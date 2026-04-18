type_matrix = {
    'Normal': ['Fighting'],
    'Fire': ['Water', 'Ground', 'Rock'],
    'Water': ['Grass', 'Electric'],
    'Grass': ['Fire', 'Ice', 'Poison', 'Flying', 'Bug']
}
# more to come

# ----- ADD METHOD TO GET TYPES FROM POKEMON

my_types = ['Fire', 'Water']

def check_weakness(t):
    for i in t:
        print(type_matrix[i])
    # return type_matrix[t]


check_weakness(my_types)