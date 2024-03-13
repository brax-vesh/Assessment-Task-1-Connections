
import random

def setup_word_categories(): # where i generate the word list for the game
    word_categories = []

    basketball_category = {
        'category name': 'Basketball',
        'words': ['Basket','Court','Team','Endline']
    }
    
    games_category = {
        'category name': 'Games',
        'words': ['Doom','Halo','Dishonored','CoD']
    }

    colours_category = {
        'category name': 'Colours',
        'words': ['Salmon','Apricot','Puke','Tan']
    }

    elements_category = {
        'category name': 'Elements',
        'words': ['Neon','Tin','Mercury','Manganese']
    }

    currency_category = {
        'category name': 'American Currency Slang',
        'words': ['Benjamin','Bucks','Moola','Bread']
    }

    coding_category = {
        'category name': 'Coding',
        'words': ['Python', 'C#', 'Java', 'Scratch Jr']
    }

    weapons_category = {
        'category name': 'Weapons',
        'words': ['Hunga Munga', 'Mancatcher', 'Morning Star', 'Sling']
    }

    word_categories.append(colours_category)
    word_categories.append(basketball_category)
    word_categories.append(games_category)
    word_categories.append(elements_category)
    word_categories.append(currency_category)
    word_categories.append(coding_category)
    word_categories.append(weapons_category)

    selected_categories = random.sample(word_categories, 4) # randomly selects the categories without having dupes
    game_categories = [] # create an empty list to store category names
    for category in selected_categories:
        game_categories.append(category['category name']) # append the 'category name' to the list
    wordlist = []
    for category in selected_categories:
        for word in category['words']:
            wordlist.append(word) # adds selected words to wordlist
            random.shuffle(wordlist) # shuffles the words in the wordlist
    return wordlist, game_categories # Return both wordlist and game_categories

def populate_grid():
    wordlist, game_categories = setup_word_categories() # calls the wordlist variable into this function
    num = 0
    Grid = [
        ["Word", "Word", "Word", "Word"],
        ["Word", "Word", "Word", "Word"],
        ["Word", "Word", "Word", "Word"],
        ["Word", "Word", "Word", "Word"]
    ]
    for row in range(len(Grid)): # cycles through the grid
        for col in range(len(Grid[row])):
            Grid[row][col] = wordlist[num] # Grid[row][col] selects a specific cell and changes the word placeholder into one of the word random word 
            num += 1
            if num >= len(wordlist):
                break
    return Grid, game_categories # Return both Grid and game_categories

grid, game_categories = populate_grid() # Receive both Grid and game_categories
for row in grid:
    print(row)

print("Selected categories:", game_categories)

def get_player_guess():
    input("Pick 4 words from the grid you think relate to eachother in this format... [word, word, word, word]...",)
    player_guess = input
    return player_guess

get_player_guess()