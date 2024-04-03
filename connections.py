
import random


def display_grid(grid, correct_guesses): # just displays the grid in a nice format  
            for row in grid:
                print(" ")
                print(row)

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
        'words': ['Salmon','Apricot','Caramel','Tan']
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
        'words': ['Python', 'C', 'Java', 'Scratch Jr']
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
    
    return wordlist, selected_categories, category1, category2, category3, category4

def update_grid(correct_guesses, guessed_categories, grid, category_to_remove, guesses, selected_categories, wordlist):
    correct_words = []
    if category_to_remove == None: 
        return selected_categories, grid, correct_words
    else:
        # rebuild the grid putting the guessed words to the top
        # pop the category out of the selected categories
        
        guessed_categories.append(category_to_remove)
        

        new_categories = []
        for i in selected_categories:
            if i != category_to_remove:
                new_categories.append(i)

        selected_categories = new_categories

        guessed_part_of_new_grid = []
        unguessed_part_of_new_grid = []

        for category in guessed_categories:
            guessed_part_of_new_grid.append(category)

        for category in selected_categories:
            unguessed_part_of_new_grid.append(category)
            
        

        words_to_remove = guessed_categories
        grid = repopulate_grid(guessed_part_of_new_grid, unguessed_part_of_new_grid)

        return selected_categories, grid, guessed_categories
    # pop or remove a dictionary if it has been guessed
    # repopulate the grid

def repopulate_grid(guessed_part, unguessed_part): # g
    num = 0
    Grid = [
        ["Word", "Word", "Word", "Word"],
        ["Word", "Word", "Word", "Word"],
        ["Word", "Word", "Word", "Word"],
        ["Word", "Word", "Word", "Word"]
    ]

        #create rows for the grid containing unguessed parts
    # flatted the unguessed part so they can be reshuffled
    wordlist = []

    for category in guessed_part:
        for word in category['words']:
            wordlist.append(word)

    for row in range(0,len(guessed_part)): # cycles through the grid
        for col in range(len(Grid[row])):
            Grid[row][col] = wordlist[num] # Grid[row][col] selects a specific cell and changes the word placeholder into one of the word random word 
            num += 1
            if num >= len(wordlist):
                break

    num = 0
    wordlist = []
    for category in unguessed_part:
        for word in category['words']:
            wordlist.append(word)
            random.shuffle(wordlist)


    for row in range(4-len(unguessed_part),4): # cycles through the grid
        for col in range(len(Grid[row])):
            Grid[row][col] = wordlist[num] # Grid[row][col] selects a specific cell and changes the word placeholder into one of the word random word 
            num += 1
            if num >= len(wordlist):
                break
            
    return Grid
    
    




def populate_grid(): # generate the grid using word categories that are contained in the setup word categories function
    wordlist, selected_categories, category1, category2, category3, category4 = setup_word_categories() # calls the wordlist variable into this function
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
    return Grid, wordlist, selected_categories, category1, category2, category3, category4 # Return both Grid and game_categories

def get_player_guess():
    guesses = []
    while len(guesses) < 4:  # Change <= to <
        guess = input("\033[94mPick a word... \033[0m")
        if guess in guesses:
            print("\033[1;31;40mDon't use duplicate words!\033[0m")
        else:
            guesses.append(guess)
    return guesses

def check_guess(selected_categories, correct_guesses):
    guesses = get_player_guess()

    low_guess = [guess.lower() for guess in guesses]
    if correct_guesses == 0:
        category1, category2, category3, category4 = selected_categories # this function acknowledges that if 1 guess is correct then there are only 3 more categories left and so on
        words1 = [word.lower() for word in category1['words']]
        words2 = [word.lower() for word in category2['words']]
        words3 = [word.lower() for word in category3['words']]
        words4 = [word.lower() for word in category4['words']]
        if all(word in words1 for word in low_guess):
            return category1, True, guesses
        elif all(word in words2 for word in low_guess):
            return category2, True, guesses
        elif all(word in words3 for word in low_guess):
            return category3, True, guesses
        elif all(word in words4 for word in low_guess):
            return category4, True, guesses
        else:
            return None, False, guesses
    elif correct_guesses == 1:
        category1, category2, category3 = selected_categories
        words1 = [word.lower() for word in category1['words']]
        words2 = [word.lower() for word in category2['words']]
        words3 = [word.lower() for word in category3['words']]
        if all(word in words1 for word in low_guess):
            return category1, True, guesses
        elif all(word in words2 for word in low_guess):
            return category2, True, guesses
        elif all(word in words3 for word in low_guess):
            return category3, True, guesses
        else:
            return None, False, guesses
    elif correct_guesses == 2:
        category1, category2 = selected_categories
        words1 = [word.lower() for word in category1['words']]
        words2 = [word.lower() for word in category2['words']]
        if all(word in words1 for word in low_guess):
            return category1, True, guesses
        elif all(word in words2 for word in low_guess):
            return category2, True, guesses
        else:
            return None, False, guesses
    elif correct_guesses == 3:
        for category in selected_categories:
            words = [word.lower() for word in category['words']]
            if all(word in words for word in low_guess):
                return category, True, guesses
            else:
                return None, False, guesses

def play_again_prompt():
    answer = input("Do you want to play again? Y/N... ")
    if answer == "Y" or answer == "y":
        playgame()   
    elif answer == "N" or answer == "n":
        print("Thanks for playing!")
        return True
    else:
        print("Please select Y or N... ")
        return False

def playgame():
    correctly_guessed_categories = []
    print(" ")
    lives = 4 # set initial guesses to 4
    correct_words = []
    correct_words.append('hello')
    correct_guesses = 0 # start correct guesses to 0
    guessed_categories = []
    grid, wordlist, selected_categories, category1, category2, category3, category4 = populate_grid() 
    display_grid(grid, correct_guesses)   
    while lives > 0 and correct_guesses < 4: # 1. display grid to the user
        category_to_remove, validate, guesses = check_guess(selected_categories, correct_guesses) # 2. get guesses and check if correct
        selected_categories, grid, correct_words = update_grid(correct_guesses, guessed_categories, grid, category_to_remove, guesses, selected_categories, wordlist)
        print(" ")
        display_grid(grid, correct_guesses)
        if lives == 2:
            print("\033[1;31;40m 1 life left!\033[0m")
        if validate == True: # adjust lives if required
            correct_guesses += 1
            print(" ")
            print ("\033[1;32;40m Correct!\033[0m")
            print("\033[1;32;40m The category was\033[0m", (category_to_remove['category name']))
            print(" ")
        elif validate == False:
            lives -= 1
            print(" ")
            print ("\033[1;31;40m Incorrect...\033[0m")
            print(" ")
    else:
        if lives == 0:
            print(" ")
            print("\033[1;31;40m You lose, game over\033[0m")
        elif correct_guesses == 4 and lives == 1:
            print(" ")
            print("\033[1;32;40m Phew! That was a close one!\033[0m")
            print("\033[1;32;40m Congratulations, you win!\033[0m")
        elif correct_guesses == 4:
            print(" ")
            print("\033[1;32;40m Congratulations, you win!\033[0m")
    answer = play_again_prompt()
    while answer == False:
        answer = play_again_prompt()

playgame()
