from bs4 import BeautifulSoup 
import requests 
import pandas as pd
import time 

# Creat global variables
def Globals():
    global race_links_list
    race_links_list = []
    global F1_list
    F1_list = []
    global counter
    counter = 0

# Connect to page
def Set_connection():
    # Define the URL of the website you want to scrape
    url = "https://www.formula1.com/en/results.html/2023/races.html"

    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page with BeautifulSoup
        print("200")

    # set up html for scraping     
    soup = BeautifulSoup(response.content, 'html.parser')

    # Make list to store links for each race event
    
    race_name_list = []
    

    # Scrape for links
    table = soup.find_all('table')[0]
    row = table.find_all('tr')[1:]

    for item in row:

        race_name = item.find_all('a')

        race_link = item.find('a', {'class' :'dark bold ArchiveLink'})['href']

        # item.find('td', {'class' : 'dark'}).text,

        # link_start = race_link[44:]

        
        race_links_list.append(race_link)


        for race in race_name:
            
            # This list could go as the name of each csv file?
            race_name_list.append(race.text.strip())
        
    
    # print(race_links_list)
    # return race_links_list
    
    
    #print(soup)
    # return soup

# Scrape race page data
def Scrape_page(x):
    
    #This sets soup = to output of Set_Connection Function
    # soup = Set_connection()
    url = f"https://www.formula1.com{x}" 
    response = requests.get(url)

    

     # set up html for scraping     
    soup = BeautifulSoup(response.content, 'html.parser')

    # find table for scraping
    table = soup.find_all('table')[0]
    # Headers for the columns of the data frame. (We will set these manually in the dictionary)
    colum_header = table.find_all('tr')[0:1]
    # Select rows of drivers race data
    row = table.find_all('tr')[1:21]
    # print(colum_header)
    
    race_name_now = f"{x[33:]}" 
    head, sep, tail = race_name_now.partition('/')
    global counter
    counter += 1

    # loop through each row for each driver
    for item in row:
         
        
        
        #Set dictionary
        F1_dict = {     
        'Race' : head,
        'Year' : "2023",
        'Race_number' : counter,
        'Position' : item.find('td', {'class' : 'dark'}).text,
        'Driver_number' : item.find('td', {'class' : 'dark hide-for-mobile'}).text,
        'First_name' : item.find('span', {'class' : 'hide-for-tablet'}).text,
        'Last_name' : item.find('span', {'class' : 'hide-for-mobile'}).text,
        'Initials' : item.find('span', {'class' : 'uppercase hide-for-desktop'}).text,
        'Car' : item.find('td', {'class' : 'semi-bold uppercase hide-for-tablet'}).text,
        'Laps' : item.find('td', {'class' : 'bold hide-for-mobile'}).text,
        'Time' : item.find_all('td', {'class' : 'dark bold'})[1].text,
        'Points' : item.find_all('td', {'class' : 'bold'})[3].text
        }

        # Append list
        F1_list.append(F1_dict)


    # return(F1_list)

    

    #pass to data frame
    df = pd.DataFrame(F1_list)
    #print(df)
    df.to_csv('/Users/robyn/Documents/GitHub/Cpp_Projects/F1_Fantasy_Game/Race data/F1_2023.csv', index = False)

# Call functions  
def main():

    Globals()
    Set_connection()
    
    #run Data scraper
    for x in race_links_list:
        Scrape_page(x)
        time.sleep(.1) 
        #print(x)
                                                                                                
    #pass to data frame
    df = pd.DataFrame(F1_list)
    #print(df)
    df.to_csv('/Users/robyn/Documents/GitHub/Cpp_Projects/F1_Fantasy_Game/Race data/2023_Season_Race_data.csv', index = False)

# Start script
main()






