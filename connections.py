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

def print_words(word_categories):
    for category in word_categories:
        for word in category['words']:
            print(word)

def setup_word_categories():
    word_categories = []

    basketball_category = {
     'category_name': 'Basketball',
     'words': ['basket','court','team','endline']
     }

    word_categories.append(basketball_category)

    return word_categories
    
print_words(setup_word_categories)
    
#test


    