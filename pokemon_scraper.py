from bs4 import BeautifulSoup
import requests
import pandas as pd


url = 'https://www.serebii.net/fireredleafgreen/kantopokedex.shtml'

page = requests.get(url)
soup = BeautifulSoup(page.text, features='html.parser')


# print(soup.find_all('td', class_ = "fooinfo"))

table = soup.find_all('table')[1]

# ------ GET POKEMON NAMES --------------
pokemon_names = table.find_all('a')
pokemon_name_table = [name.text.strip() for name in pokemon_names]

while "" in pokemon_name_table:
    pokemon_name_table.remove("")


p_names = []
for i in pokemon_name_table:
    try: 
        i.encode(encoding='utf-8').decode('ascii')      # if character contains Jpanese characters
 
    except UnicodeDecodeError:
        i = i.encode('ascii', 'ignore').decode()        # ignore japanese chars
        p_names.append(i)


# ------ GET POKEMON IDs --------------
pokemon_table = table.find_all('td')
pokemon_table = [i.text.strip() for i in pokemon_table]
p_id = [i for i in pokemon_table if '#' in i]

# ------ GET POKEMON TITLES --------------
p_titles = pokemon_table[:12]       # get all titles (first 12 table items)
remove_titles = ['Pic', 'Abilities', 'Base Stats', 'HP', 'Att', 'Def', 'S.Att', 'S.Def', 'Spd']         # the titles to be removed
p_titles = [i for i in p_titles if i not in remove_titles]              # keep titles not in the remove list

# ------ GET POKEMON TYPES --------------

table2 = soup.find_all('table')[1]
pokemon_type = table2.find_all('tr', recursive =False)[1:]


print(pokemon_type[2])