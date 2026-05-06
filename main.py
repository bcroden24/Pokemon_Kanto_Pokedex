from pokemon_scraper import pokemon
from constants import DATABASE_URL
import pandas as pd
from sqlalchemy import create_engine

#import the pokemon dict from scraper program
pokemon_data = pokemon

# get the headers
headers = pokemon_data[0].keys()

# create dataframe to store pokemon data
df = pd.DataFrame(pokemon_data)

# type conversions
df['HP'] = df['HP'].astype('Int32')
df['Att'] = df['Att'].astype('Int32')
df['Def'] = df['Def'].astype('Int32')
df['S.Att'] = df['S.Att'].astype('Int32')
df['S.Def'] = df['S.Def'].astype('Int32')
df['Spd'] = df['Spd'].astype('Int32')

# create sql engine
engine = create_engine(DATABASE_URL)

# connect to db and create kanto pokedex table
df.to_sql('kanto_pokedex', con=engine, if_exists='replace', index=False)





weakness_matrix = {
    'Bug': ['Fire', 'Flying', 'Rock'],
    'Dark': ['Bug', 'Fighting'],
    'Dragon': ['Dragon', 'Ice'],
    'Electric': ['Ground'],
    'Fighting': ['Flying', 'Psychic'],
    'Fire': ['Ground', 'Rock', 'Water'],
    'Flying': ['Electric', 'Ice', 'Rock'],
    'Ghost': ['Dark', 'Ghost'],
    'Grass': ['Bug', 'Fire', 'Flying', 'Ice', 'Poison'],
    'Ground': ['Grass', 'Ice', 'Water'],
    'Ice': ['Fighting', 'Fire', 'Rock', 'Steel'],
    'Normal': ['Fighting'],
    'Poison': ['Ground', 'Psychic'],
    'Psychic': ['Bug', 'Dark', 'Ghost'],
    'Rock': ['Fighting', 'Grass', 'Ground', 'Steel', 'Water'],
    'Steel': ['Fighting', 'Fire', 'Ground'],
    'Water': ['Electric', 'Grass']
    }