#create word categories

#Randomly select 4-word groups from a predetermined list when the game is started.

#Display the selected word groups in a grid format in the command line.

#Set lives to 4.

#Randomise the locations of the location of the words in the grid.	

#Capture the players 4 coordinate guesses through command line.

#Allow player to access ‘hint’ command to draw a random predetermined hint for one of the four active word groups topics.

#Validate guesses and move collate the correctly guessed word groups at the top of the grid, upon correctly guessing all word groups correctly, conclude game.

#Track the incorrect guesses, notify player if they were one word off being correct, revoke 1 life for each incorrect guess, upon reaching 0 lives conclude game.

#Allow starting game once current one has concluded.


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
    wordlist = []
    for category in selected_categories:
        for word in category['words']:
            wordlist.append(word) # adds selected words to wordlist
            for category in selected_categories:
                random.shuffle(wordlist) # shuffles the words in the wordlist
    return wordlist

def populate_grid():
    wordlist = setup_word_categories() # calls the wordlist variable into this function
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
    return Grid   

grid = populate_grid()
for row in grid:
    print(row)