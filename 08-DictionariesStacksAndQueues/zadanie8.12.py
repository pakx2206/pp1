import json
favourite = {
    'title': 'The Lord of the Rings',
    'author': 'J.R.R. Tolkien',
    'year_released': 1954,
    'genre': 'Fantasy',
    'main_character': 'Frodo Baggins'
}
with open("08-DictionariesStacksAndQueues/favourite.json", 'w') as f:
    json.dump(favourite, f, indent=6)
