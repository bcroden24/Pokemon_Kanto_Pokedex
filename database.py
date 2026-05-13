from pokemon_scraper import pokemon
from constants import DATABASE_URL
import pandas as pd
from sqlalchemy import create_engine, text

# create sql engine
engine = create_engine(DATABASE_URL)

def create_database_load_data():
    # import the pokemon dict from scraper program
    
    pokemon_data = pokemon
    # get the headers
    
    # headers = pokemon_data[0].keys()

    # create dataframe to store pokemon data
    df = pd.DataFrame(pokemon_data)
    # type conversions
    df['HP'] = df['HP'].astype('Int32')
    df['Att'] = df['Att'].astype('Int32')
    df['Def'] = df['Def'].astype('Int32')
    df['S.Att'] = df['S.Att'].astype('Int32')
    df['S.Def'] = df['S.Def'].astype('Int32')
    df['Spd'] = df['Spd'].astype('Int32')

    # add try/catch ?

    # connect to db and create kanto pokedex table
    df.to_sql('kanto_pokedex', con=engine, if_exists='replace', index=False)


# get data from database
def fetch_pokemon_data(p):
    df = pd.read_sql(f"SELECT * FROM kanto_pokedex WHERE \"Name\" = \'{p}\'", engine)
    return df
    

