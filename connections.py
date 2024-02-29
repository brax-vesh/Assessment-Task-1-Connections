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


Grid = [
    ["Word","Word","Word","Word"],
    ["Word","Word","Word","Word"],
    ["Word","Word","Word","Word"],
    ["Word","Word","Word","Word"],
]
#this is the empty grid that will be populated with my words

def print_words(word_categories): #was using this to test my category dictionaries were working
    for category in word_categories:
        for word in category['words']:
            print(word)

def setup_word_categories(): #this function is where I store all my categories
    global word_categories
    word_categories = []

    basketball_category = {
     'category name': 'Basketball',
     'words': ['Basket','Court','Team','Endline']
     }
    
    games_category = {
        'category name': 'Games',
        'words': ['Doom','Halo','Dishonered','CoD']
    }

    colours_category = {
        'category name': 'Colours',
        'words:': ['Salmon','Apricot','Puke','Tan']
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
        'category name': ''
    }

    
    word_categories.append(colours_category)
    word_categories.append(basketball_category)
    word_categories.append(games_category)
    word_categories.append(elements_category)
    word_categories.append(currency_category)
    word_categories.append(coding_category)

def select_categories(): #working on this, will return randomly selected categories to be used for populating the grid the player views
    return chosen_categories

    
def populate_grid(word_categories): #working on this, will populate grid with randomly selected categories
row = 0


def get_guess(): # Gets guess imput from player and returns value entered

    guess = input("Please enter 4 words you think fit under the same category...")
    return guess



    
