
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
        'words': ['Neon','Tin','Mercury','Aluminium']
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
    
    selected_categories = random.sample(word_categories, 4) # Randomly select 4 categories without duplicates

    # Separate variables for each selected category
    category1, category2, category3, category4 = selected_categories

    wordlist = []
    for category in selected_categories:
        for word in category['words']:
            wordlist.append(word)
            random.shuffle(wordlist)
    
    return wordlist, category1, category2, category3, category4

def populate_grid():
    wordlist, category1, category2, category3, category4 = setup_word_categories() # calls the wordlist variable into this function
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
    return Grid, category1, category2, category3, category4 # Return both Grid and game_categories

def get_player_guess():
    guesses = []
    for i in range(4):
        guess = input("type a word...")
        guesses.append(guess)
    return guesses

def check_guess():
    guesses = get_player_guess()
    _, category1, category2, category3, category4 = populate_grid()
    words1 = [word.lower() for word in category1['words']]
    words2 = [word.lower() for word in category2['words']]
    words3 = [word.lower() for word in category3['words']]
    words4 = [word.lower() for word in category4['words']]

    low_guess = [guess.lower() for guess in guesses]

    if all(word in words1 for word in low_guess):
        return True
    elif all(word in words2 for word in low_guess):
        return True
    elif all(word in words3 for word in low_guess):
        return True
    elif all(word in words4 for word in low_guess):
        return True
    
    return False
        


def action():
    correct = check_guess()
    if correct == True:
        print('right')
    else:
        print('wrong')

grid, category1, category2, category3, category4  = populate_grid()

for row in grid:
    print(row)

action()



