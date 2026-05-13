from database import *
from types_matrix import *
from collections import Counter

# create_database_load_data()

# ----- NEXT STEPS - ADD GUI FEATURE i.e bar chart


def get_data():

    while True:

        p_name = input("Enter name of your Pokemon:  ").capitalize()
        p_data = fetch_pokemon_data(p_name)

        if p_data.empty:
            print("Pokemon Not found. Please try again.")
        else:
            # convert from pandas series to a string.
            # clean string to get only types in a list
            p_types = p_data['Types'].to_string().partition('{')[2].partition('}')[0].split(',')
            print("Success!")
            return p_types
        

def get_party():
    party = []
    # Get party of 6 pokemon
    while len(party) < 6:
        party.append(get_data())

    return party


# main loop

def main():
    party = get_party()
    # party = [['Fire', 'Flying'], ['Electric'], ['Rock', 'Ground'], ['Psychic'], ['Water', 'Ice'], ['Grass', 'Poison']]
    
    weakness_results = []
    for i in party:
        for j in i:
            res = check_weakness(j, weakness_matrix)
            for i in res:
                weakness_results.append(i)


    # print(weakness_results)

    count = Counter(weakness_results)
    print(count)



main()