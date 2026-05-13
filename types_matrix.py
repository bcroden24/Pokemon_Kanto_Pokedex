types_list = ['Bug','Dark','Dragon','Electric','Fighting','Fire','Flying','Ghost','Grass','Ground','Ice','Normal','Poison','Psychic','Rock','Steel','Water']

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

# ----- ADD METHOD TO GET TYPES FROM POKEMON

# my_types = ['Fire', 'Water']

# check weakness types using type dict, return values of the whichever key matches input value t
def check_weakness(t, weakness):
    return weakness[t]
        
# Use weakness dict to find strong against types, return keys which values include input value t
def check_strength(t, weakness):
    keys = [k for k, v in weakness.items() if t in v]
    return keys

# prints check weakness/strength results
def get_type_effectiveness(t, weakness):
    weak_against = check_weakness(t, weakness)
    strong_against = check_strength(t, weakness)

    print(f"Your Pokemon is strong against {strong_against}\nYour Pokemon is weak against {weak_against}")

# get_type_effectiveness('Water', weakness_matrix)