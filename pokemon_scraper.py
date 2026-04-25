# This program intends to pull html data from https://www.serebii.net/fireredleafgreen/kantopokedex.shtml
# Using BeautifulSoup to parse html data grabbing rows relating to Pokemon data
# Cleaning individual row data and structuring data into a dictionary
# Pokemon dictionary stores data for all pokemon in Kanto Pokedex


from bs4 import BeautifulSoup
import requests
import pandas as pd


url = 'https://www.serebii.net/fireredleafgreen/kantopokedex.shtml'

page = requests.get(url)
soup = BeautifulSoup(page.text, features='html.parser')

table = soup.find_all('table')[1]

pokemon_data = table.find_all('tr', recursive =False)[1:]       # get all rows inside table but not recursive - to keep rows modular and consistent


data = []   # stores all rows for each pokemon
for row in pokemon_data[1:]:
    row_data = row.find_all('td')   # find each td in each row

    individual_row_data = [data.text.strip() for data in row_data] # clean text in each piece of data in row
    data.append(individual_row_data)                               # append cleaned row data to list

# remove empty items from list
for row in data:
    while "" in row:
        row.remove("")

# remove Japanese characters from pokmemon names
for row in data:
    try:
        row[1].encode(encoding='utf-8').decode('ascii')
    
    except UnicodeDecodeError:
        row[1] = row[1].encode('ascii', 'ignore').decode()


pokemon = []
# create dictionary to store and format data in key:value pairs for each pokemon
for p in data:
    pokemon.append({
        'Pokedex ID': p[0],
        'Name': p[1],
        'Abilities': p[2],
        'HP': p[3],
        'Att': p[4],
        'Def': p[5],
        'S.Att': p[6],
        'S.Def': p[7],
        'Spd': p[8]
    })
   


