from pokemon_scraper import pokemon
from constants import DATABASE_URL
import pandas as pd
from sqlalchemy import create_engine

#import the pokemon dict from scraper program
pokemon_data = pokemon

# for pokemon in pokemon_data:
#     print(pokemon)

headers = pokemon_data[0].keys()


df = pd.DataFrame(pokemon_data)

df['HP'] = df['HP'].astype('Int32')
df['Att'] = df['Att'].astype('Int32')
df['Def'] = df['Def'].astype('Int32')
df['S.Att'] = df['S.Att'].astype('Int32')
df['S.Def'] = df['S.Def'].astype('Int32')
df['Spd'] = df['Spd'].astype('Int32')

# print(df)

engine = create_engine(DATABASE_URL)

df.to_sql('kanto_pokedex', con=engine, if_exists='replace', index=False)





