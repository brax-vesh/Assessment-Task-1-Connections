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
    return wordlist, selected_categories

def printington():
    selected_categories = setup_word_categories
    setup_word_categories()
    print(selected_categories)

printington()