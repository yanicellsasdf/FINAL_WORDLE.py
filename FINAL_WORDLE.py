#HEADER HERE PLEASE DOUBLE CHEKC IF SAKTO AND PLEASE CHANGE THE DATE

# Edrian Miguel E. Capistrano
# 240939
# August 27, 2024

# I have not discussed the Python language code in my program
# with anyone other than my instructor or the teaching assistants
# assigned to this course.

# I have not used Python language code obtained from another student,
# or any other unauthorized source, either modified or unmodified.

# If any Python language code or documentation used in my program
# was obtained from another source, such as a textbook or website,
# that has been clearly noted with a proper citation in the comments
# of my program.

import random

random_words = ["SERIF", "DERBY", "GHOST", "APPLE", "BRAVE", "CLASH", "DRAIN", "EAGER", "FLICK", "GRASP", "HEART", "IGLOO", "JUMPY", "KNACK", "LATCH", "MINTY", "NUDGE", 
                "OASIS", "PLEAD", "QUEEN", "RANCH", "SHARP", "TANGO", "UPPER", "VIVID", "WORTH", "YEARN", "ZEBRA", "ALIGN", "BATCH", "CRISP", "DAISY", "ELDER", "FLARE", 
                "GLOWN", "HELIX", "INLET", "JOINT", "KNEAD", "LODGE", "MARCH", "NOBLE", "ORBIT", "PLANK", "QUIET", "REACT", "SWIFT", "TRAIL", "UNITY", "VOTER", "WRIST", 
                "YIELD", "AZURE", "BLESS", "CRUMB", "DRIVE", "EQUIP", "FLINT", "GRAPE", "HAUNT", "IVORY", "JOLLY", "KNIFE", "LEMON", "MAGIC", "NEIGH", "OPERA", "PULSE", 
                "QUAKE", "ROBIN", "STORM", "THINK", "UPSET", "VALVE", "WAGON", "YOUTH", "ZONAL", "ALIVE", "BLOCK", "CROWN", "DUSTY", "ENEMY", "FRESH", "GLASS", "HONEY", 
                "INDEX", "JOKER", "LAYER", "MOTOR", "NIGHT", "OCEAN", "PAINT", "QUOTA", "ROAST", "SMILE", "THUMB", "ULTRA", "VIRUS", "WOVEN", "YACHT", "ZESTY"]

uppercase_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def pseudo_upper(word):
    temp = []
    for item in word:
        pseudo_index = 0
        caps = True
        for letter in lowercase_alphabet:
            if item == letter:
                temp.append(uppercase_alphabet[pseudo_index])
                caps = False
                break
            pseudo_index += 1

        if caps is True:
            temp.append(item)
        
    word = ""
    for item in temp:
        word += str(item)
    return word

def show_alphabet(word, unused, used, display):
    for k in range(len(word)):
        for l in range(len(unused)):
            if word[k] == unused[l]:
                used[l] = False  
                break

    display = [unused[item] for item in range(len(used)) if used[item] is not False]
    return display

def update_display(values_list):
    output = ""
    for value in values_list:
        if value == -2:
            output += "_"
        else:
            output += str(value)
    return output

def wordle():
    while True:
        word_to_guess = input("\nPlease enter a word for the player to guess: \n")
        length_of_word_to_guess = len(word_to_guess)
        word_to_guess = pseudo_upper(word_to_guess)

        if word_to_guess == "RANDOM":
            pick_random = int((random.random() * 100))
            word_to_guess = random_words[pick_random]
            length_of_word_to_guess = len(word_to_guess)
            break
        elif word_to_guess == "QUIT":
            print("\nThank you for playing Wordle!")
            return False
        elif length_of_word_to_guess != 5:
            print("\nThe word must contain exactly 5 letters only")
            continue
        else:
            break

    #REMOVE THIS IN FINAL
    print(word_to_guess)
    
    to_display = []
    alphabet_check = ""
    alphabet_used = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    to_display = [-2 for item in range(length_of_word_to_guess)]

    change_lives = pseudo_upper(input("\nDo you want to change the number of guesses? If no, the number of guesses you will have is automatically set to 6. Type 'Y' for yes or 'N' for no.\n"))

    if change_lives == 'Y':
        new_lives = int(input("\nEnter how many guesses you want to have:\n"))
        n = new_lives
    elif change_lives == 'N':
        n = 6

    game_over = True

    while game_over:
        used_word_to_guess = [False for item in range(length_of_word_to_guess)]
        used_user_guess = [False for item in range(length_of_word_to_guess)]

        while True:
            user_guess = input(f"\nGuess the word, {n} blank guess(es) left: {update_display(to_display)} \n")
            user_guess = pseudo_upper(user_guess)
     
            if user_guess == "ALPHABET":
                alphabet_show = []
                print(show_alphabet(alphabet_check, uppercase_alphabet, alphabet_used, alphabet_show))
                continue
            else:
                alphabet_check += user_guess
                break

        to_display = [-2 for item in range(length_of_word_to_guess)]
        
        if user_guess == word_to_guess:
            game_over = False
            print("\nCongratulations! You Win!")
            break

        for i in range(length_of_word_to_guess):
            if word_to_guess[i] == user_guess[i]:
                to_display[i] = word_to_guess[i]
                used_word_to_guess[i] = True
                used_user_guess[i] = True

        for i in range(length_of_word_to_guess):
            if not used_user_guess[i]:
                for j in range(length_of_word_to_guess):
                    if not used_word_to_guess[j] and user_guess[i] == word_to_guess[j]:
                        to_display[i] = "!"
                        used_word_to_guess[j] = True
                        break
                if to_display[i] == -2:
                    to_display[i] = "?"

        n -= 1
        
        if n == 0:
            game_over = False
            print("\nSORRY, YOU LOSE")

while True:
    if wordle() is False:
        break
        