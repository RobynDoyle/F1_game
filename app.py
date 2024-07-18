from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error
import random

app = Flask(__name__)

def total_racesz():
    race_names = ["bahrain", "saudi-arabia", "australia", "azerbaijan", "miami", "monaco", "spain", "canada", "austria", "great-britain", "hungary", "belgium", "netherlands", "italy", "singapore", "japan", "qatar", "united-states", "mexico", "brazil", "las-vegas", "abu-dhabi"]
    races_uppercase_list = [item.upper() for item in race_names]
    return races_uppercase_list

def get_current_race(races, race_counter, total_races):
    
    Races_this_session = []
    
    for i in range(0,int(races)):
        Races_this_session.append(total_races[i])

    current_race = Races_this_session[race_counter]
    return current_race

def get_current_race_picture(race_counter):
    Races_picture = list(range(22))
    path_to_pic = url_for('static', filename=f'images/{Races_picture[race_counter]}.jpg')
    this_race_picture = path_to_pic
    return this_race_picture

def query_with_variables(race_counter, Driver, Driver_two, Driver_three):
  

    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='P@ssw0rd',
            database='F1'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            query = "SELECT Points FROM F1_2023 WHERE (Race_number = %s AND Initials = %s) OR (Race_number = %s AND Initials = %s) OR (Race_number = %s AND Initials = %s) "
            cursor.execute(query, (race_counter+1, Driver, race_counter+1, Driver_two, race_counter+1, Driver_three))
            rows = cursor.fetchall()
            cursor.close()
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            connection.close()
    points_counter = 0
   
    for tup in rows:
        points_counter += sum(tup)
        print(points_counter)
        
    return points_counter

def query_for_driver_list(Race_counter):
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='P@ssw0rd',
            database='F1'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            query = "SELECT Initials FROM F1_2023 WHERE (Race_number = %s)"
            cursor.execute(query, (Race_counter+1,))
            driver_list_out = cursor.fetchall()
            cursor.close()
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            connection.close()
    Driver_clean_list = [driver[0] for driver in driver_list_out]
    return Driver_clean_list

def Select_driver(Race_counter):
    Driver_list = query_for_driver_list(Race_counter)
    return Driver_list

def AI_Select_driver(Count, Difficulty):

    Driver_list = query_for_driver_list(Count)
    

    AI_DRIVER_one = "SAME"
    AI_DRIVER_two = "SAME"
    AI_DRIVER_three = "SAME"

    # randomly picks a driver from list - increase number to increase the difficulty
    while (AI_DRIVER_one not in Driver_list): 
            pick_one = random.randint(0, (len(Driver_list)-Difficulty))
            AI_DRIVER_one = Driver_list[pick_one]
            AI_DRIVER_one= AI_DRIVER_one.upper()
    while (AI_DRIVER_two not in Driver_list) or (AI_DRIVER_two == AI_DRIVER_one): 
            pick_two = random.randint(0, (len(Driver_list)-Difficulty))
            AI_DRIVER_two = Driver_list[pick_two]
            AI_DRIVER_two= AI_DRIVER_two.upper()
    while (AI_DRIVER_three not in Driver_list) or (AI_DRIVER_three == AI_DRIVER_one) or (AI_DRIVER_three == AI_DRIVER_two): 
            pick_three = random.randint(0, (len(Driver_list)-Difficulty))
            AI_DRIVER_three = Driver_list[pick_three]
            AI_DRIVER_three= AI_DRIVER_three.upper()
    

    # Query for point for AI player
    AI_results = query_with_variables(Count, AI_DRIVER_one, AI_DRIVER_two, AI_DRIVER_three)
    return AI_results, AI_DRIVER_one, AI_DRIVER_two, AI_DRIVER_three

# ________________________________________FLASK PART_____________________________________________________________

@app.route('/', methods=['GET', 'POST'])
def home():
    
    return render_template('index.html')

@app.route('/start', methods=['GET', 'POST'])
def start():
    
    race_counter = 0
    points = 0
    ai_points = 0
    
    if request.method == 'POST':
        player_name = request.form['player_name'].upper()
        # player_name = 
        races = request.form['races']
        difficulty_check = request.form['difficulty']

        if difficulty_check == "HARD":
            difficulty = 14
        elif difficulty_check == "MEDIUM":
            difficulty = 10
        else:
            difficulty = 6

        # Redirect to the select_driver page with player_name in the query string
        return redirect(url_for('select_driver', difficulty_check=difficulty_check, ai_points=ai_points, points=points, player_name=player_name, races=races, difficulty=difficulty, race_counter=race_counter))
    return render_template('start.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/credit', methods=['GET', 'POST'])
def credit():
    return render_template('credit.html')

@app.route('/select_driver', methods=['GET', 'POST'])
def select_driver():
    if request.method == 'GET':
        race_counter = request.args.get('race_counter', type=int)
        ai_points = request.args.get('ai_points', type=int)
        races = request.args.get('races', type = int)
        player_name = request.args.get('player_name') #Shows playername
        difficulty_check = request.args.get('difficulty_check')
        difficulty = request.args.get('difficulty', type = int) #Outputs chose difficulty of this session
        points = request.args.get('points', type = int)
         
    if request.method == 'POST':
        race_counter = request.form.get('race_counter', type=int)
        races = request.form.get('races', type=int)
        ai_points = request.form.get('ai_points', type=int)
        player_name = request.form.get('player_name')
        difficulty_check = request.form.get('difficulty_check')
        difficulty = request.form.get('difficulty', type = int)
        
        points = request.form.get('points', type=int)
         
  
    total_races = []
    total_races += total_racesz()

    if race_counter >= races:  # Check if race_counter reaches the number of races
        champion = "bob"
        if ai_points == points:
            champion = player_name + "tied with Computer"
        elif ai_points > points:
            champion = "Computer"
        else:
            champion = player_name
        return render_template('end.html', champion=champion, difficulty_check=difficulty_check, ai_points=ai_points, player_name=player_name, points=points, races=races, difficulty=difficulty)

    driver_list = Select_driver(race_counter)
    current_race = get_current_race(races, race_counter, total_races) #Gets name of current race 
    this_race_picture = get_current_race_picture(race_counter) #Gets different picture for each race
    
        
    return render_template('select_driver.html', ai_points=ai_points, race_counter=race_counter, player_name=player_name, races=races,
                           difficulty=difficulty, current_race=current_race, points=points, difficulty_check=difficulty_check, 
                           this_race_picture=this_race_picture, driver_list=driver_list )
      
@app.route('/ai', methods=['GET', 'POST'])
def ai():
        
    if request.method == 'POST':
        race_counter = request.form.get('race_counter', type=int)
        races = request.form.get('races', type=int)
        difficulty_check = request.form.get('difficulty_check')
        player_name = request.form.get('player_name')
        difficulty = request.form.get('difficulty', type = int)
        points = request.form.get('points', type = int)
        Driver = request.form.get('driver')
        Driver_two = request.form.get('driver_two')
        Driver_three = request.form.get('driver_three')
        ai_points = request.form.get('ai_points', type=int)
        
        ai_list = AI_Select_driver(race_counter, difficulty)
        ai_points += ai_list[0]

        ai_drivers = ai_list[1:]

        points = request.form.get('points', type=int)
        points += query_with_variables(race_counter, Driver, Driver_two, Driver_three) 

    total_races = []
    total_races += total_racesz()
    driver_list = Select_driver(race_counter)
    
    current_race = get_current_race(races, race_counter, total_races) #Gets name of current race
    
    this_race_picture = get_current_race_picture(race_counter) #Gets different picture for each race
    return render_template('ai.html', ai_drivers=ai_drivers, difficulty_check=difficulty_check, ai_points=ai_points, race_counter=race_counter, points=points, player_name=player_name, races=races, difficulty=difficulty, current_race=current_race, this_race_picture=this_race_picture, driver_list=driver_list )

@app.route('/result', methods=['GET', 'POST'])
def result():
   
    if request.method == 'POST':
        race_counter = request.form.get('race_counter', type=int)
        races = request.form.get('races', type=int)
        difficulty_check = request.form.get('difficulty_check')
        player_name = request.form.get('player_name')
        difficulty = request.form.get('difficulty', type = int)
        ai_points = request.form.get('ai_points', type=int)
        points = request.form.get('points', type = int)
    
    total_races = []
    total_races += total_racesz()
    driver_list = Select_driver(race_counter)
    
    current_race = get_current_race(races, race_counter, total_races) #Gets name of current race
    
    this_race_picture = get_current_race_picture(race_counter) #Gets different picture for each race
    race_counter += 1
    return render_template('result.html', ai_points=ai_points, difficulty_check=difficulty_check, race_counter=race_counter, points=points, player_name=player_name, races=races, difficulty=difficulty, current_race=current_race, this_race_picture=this_race_picture, driver_list=driver_list )

if __name__ == '__main__':
    app.run(debug=True)