import random

def main():
    print("WELCOME TO WORD GUESSER!")
    print("Can you guess the word?")

    user_Difficulty = setDifficulty() #Get user difficulty

    if user_Difficulty == 1:
        chalEasy()
    elif user_Difficulty == 2:
        chalHard()

def setDifficulty():
    main_Menu = True
    set_difficulty = 0

    while main_Menu:
        try:
            choice_Difficulty = int(input("Please select your difficulty: \n"
                                          "1. Easy\n"
                                          "2. Hard\n"))
            if choice_Difficulty == 1:
                set_difficulty = 1
                break
            elif choice_Difficulty == 2:
                set_difficulty = 2
                break
            else:
                print("Please select a valid difficulty.\n")
        except ValueError:
            print("Please enter a number.")

    return set_difficulty

def chalEasy():

    #Word Dictionaries
    dict_Words: dict = {
        'Apple': "Five letter word. This fruit can be red or green. It's commonly sold as juice. It grows in trees!",
        'Banana': "Six letter word. It's yellow and grows in trees!",
        'Orange': "Six letter word. The color matches the name! Commonly used as a breakfast beverage.",
        'Pineapple': "Nine letter word. Who lives in a pineapple under the sea?"
    }

    dict_words_hint: dict = {
        'Apple': "Granny Smith!",
        'Banana': "Shaped like a crescent moon",
        'Orange': "It's shaped like a sphere.",
        'Pineapple': "Spongebob Squarepants!"
    }

    #Word Variables
    target_fruit = random.choice(list(dict_Words.keys())) #Random Word
    target_fruit_clue = dict_Words[target_fruit] #Grabs the clue for the word at the key
    target_fruit_hint = dict_words_hint[target_fruit] #Grab the hint for the word at the key

    #User Lives
    user_Lives: int = 6

    print(f"You have {user_Lives} lives left.\n"
          f"Capitalization does not matter. Spaces DO matter.\n"
          f"Category is fruit!\n")

    guess_Menu = True
    while guess_Menu:
        print(f"I'm thinking of a fruit. Your clue is: {target_fruit_clue}")
        user_Guess = input("Please enter your guess: ")
        if user_Guess.lower() == target_fruit.lower():
            print(f"Congratulations! The fruit was {target_fruit}!\n")
            input("Press any key to exit the game...")
            exit(0)
        elif user_Guess == "hint":
            print(f"{target_fruit_hint}\n")
        else:
            print("Guess incorrect. -1 Life. Try again.\n")
            user_Lives -= 1

        if user_Lives == 0:
            print("Game Over!\n"
                  f"Your fruit was {target_fruit}!")
            input("Press any key to exit the game...")
            exit(0)

def chalHard():

    #Word Dictionaries
    dict_Words: dict = {
        'Twilight': "Hairy dog man fights immortal bat for their love's hand in marriage.",
        'Guardians of the Galaxy': "Talking raccoon teams up with the God of Thunder, a mercenary, and an outerspace strong man.",
        'Warcraft': "Based off of the most popular MMO from Blizzard Entertainment. This movie presented a fight between Orcs and Humans.",
        'Saving Private Ryan': "Starring Forrest Gump as the lieutenant of this movie, Forrest was a teacher before he was sent to find someone."
    }


    dict_words_hint: dict = {
        'Twilight': "#Team...",
        'Guardians of the Galaxy': "The crew includes a talking tree.",
        'Warcraft': "LEROOOOOY!......JENKINS!",
        'Saving Private Ryan': "It's a war movie from the 1980s."
    }

    #Word Variables
    target_movie = random.choice(list(dict_Words.keys())) #Random Word
    target_movie_clue = dict_Words[target_movie] #Grabs the clue for the word at the key
    target_movie_hint = dict_words_hint[target_movie] #Grab the hint for the word at the key

    #User Lives
    user_Lives: int = 3

    print(f"You have {user_Lives} lives left.\n"
          f"Capitalization does not matter. Spaces DO matter.\n"
          f"Category is Movies!\n")

    guess_Menu = True
    while guess_Menu:
        print(f"I'm thinking of a movie. Your clue is: {target_movie_clue}")
        user_Guess = input("Please type your guess: ")
        if user_Guess.lower() == target_movie.lower():
            print(f"Congratulations! The movie was {target_movie}!\n")
            input("Press any key to exit the game...")
            exit(0)
        elif user_Guess == "hint":
            print(f"{target_movie_hint}\n")
        else:
            print("Guess incorrect. -1 Lives. Try again.\n")
            user_Lives -= 1

        if user_Lives == 0:
            print("Game Over!\n"
                  f"Your movie was {target_movie}!")
            input("Press any key to exit the game...")
            exit(0)


if __name__ == '__main__':
    main()
