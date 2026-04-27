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

# print(pokemon_data)

data = []   # stores all rows for each pokemon
for row in pokemon_data[1:]:
    row_data = row.find_all('td')   # find each td in each row


    individual_row_data = [data.text.strip() for data in row_data] # clean text in each piece of data in row


    # get images and format them to keep only the type text
    # add to a nested types list and apppend to the final indicidual row list
    type_data = row.find_all('img')
    types = []
    for img in type_data:
        
        if img.get('src').endswith('gif'):
            # print(img.get('src'))
            types.append(img.get('src').split("/")[3].removesuffix('.gif'))
            individual_row_data.append(types)

    data.append(individual_row_data)                               # append cleaned row data to list

# if type nested list length is greater than 2 then remove it
# this is to remove duplicated nested type list from the row
for row in data:
    if(len(row[-1]) == 2):
        row.pop()

        

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
        'Spd': p[8],
        'Types': p[9]
    })
   


