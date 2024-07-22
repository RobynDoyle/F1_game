from bs4 import BeautifulSoup 
import requests
import pandas as pd

def Set_connection():
    # Define the URL of the website you want to scrape
    url = "https://www.formula1.com/en/results.html/2023/races/1141/bahrain/race-result.html"

    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page with BeautifulSoup
        print("200")

    # set up html for scraping     
    soup = BeautifulSoup(response.content, 'html.parser')
    
    #print(soup)
    return soup

def Scrape_page():
    
    #This sets soup = to output of Set_Connection Function
    soup = Set_connection()
    # find table for scraping
    table = soup.find_all('table')[0]
    # Headers for the columns of the data frame. (We will set these manually in the dictionary)
    colum_header = table.find_all('tr')[0:1]
    # Select rows of drivers race data
    row = table.find_all('tr')[1:21]
    # print(colum_header)
    # print(row)
    
    
    #Set list
    F1_list = []

    # loop through each row for each driver
    for item in row:
         
        """  position = item.find('td', {'class' : 'dark'}).text,
        driver_number = item.find('td', {'class' : 'dark hide-for-mobile'}).text,
        driver_first_name = item.find('span', {'class' : 'hide-for-tablet'}).text,
        driver_last_name = item.find('span', {'class' : 'hide-for-mobile'}).text,
        driver_initials = item.find('span', {'class' : 'uppercase hide-for-desktop'}).text,
        car = item.find('td', {'class' : 'semi-bold uppercase hide-for-tablet'}).text,
        laps = item.find('td', {'class' : 'bold hide-for-mobile'}).text,
        time_retired = item.find_all('td', {'class' : 'dark bold'})[1].text,
        points = item.find_all('td', {'class' : 'bold'})[3].text,

        print(points)"""
        
        #Set dictionary
        F1_dict = {  
        'Race' : "Bahrain 2023",    
        'Position' : item.find('td', {'class' : 'dark'}).text,
        'Driver number' : item.find('td', {'class' : 'dark hide-for-mobile'}).text,
        'First name' : item.find('span', {'class' : 'hide-for-tablet'}).text,
        'Last name' : item.find('span', {'class' : 'hide-for-mobile'}).text,
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
    df.to_csv('/Users/robyn/Documents/GitHub/Cpp_Projects/F1_Fantasy_Game/Bahrain_2023.csv', index = False)

def main():

    # Scrape page
    Scrape_page()

# Start script
main()






