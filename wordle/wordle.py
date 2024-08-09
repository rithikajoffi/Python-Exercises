# Exercise Name:
# 	10-wordle
# Description:
# 	Create the wordle game
# Resources:
# 	Valid Words List: https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93
    
import random
import requests
from colorama import Back, Style, init

# Initialize colorama
init(autoreset=False)  # Disable auto-reset to manually control where resets occur

GRAY_BG = '\033[48;5;240m' 

def fetch_words_from_gist():
    try:
        url = 'https://gist.githubusercontent.com/dracos/dd0668f281e685bad51479e5acaadb93/raw/6bfa15d263d6d5b63840a8e5b64e04b382fdb079/valid-wordle-words.txt'
        response = requests.get(url, verify = False)
        response.raise_for_status()  

        words = response.text.splitlines()  

        return words
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Gist content: {e}")
        return None

def get_random_word(words):
    return random.choice(words)

def get_feedback(guess, answer):
    feedback = []
    for g, a in zip(guess, answer):
        if g == a:
            feedback.append(Back.GREEN + g.upper())
        elif g in answer:
            feedback.append(Back.YELLOW + g.upper())
        else:
            feedback.append(GRAY_BG + g.upper())
    # Explicitly reset color to default after feedback
    return ''.join(feedback) + Style.RESET_ALL

def wordle():
    words = fetch_words_from_gist()

    if words is None:
        print("Failed to fetch words from Gist.")
        return
    
    print("\n\n\n\nWORDLE!!")
    print("!!RULES!!")
    print("The goal of Wordle is to guess a hidden five-letter word within six attempts")
    print("You have a total of six attempts to guess the correct word.")
    print("After each guess, the game will provide feedback by marking each letter:")
    print("(Green): Correct Letter and Position")
    print("(Yellow): Correct Letter, Wrong Position")
    print("(White): Incorrect Letter")

    answer = get_random_word(words)
    attempts = 6
    print("\nGuess the 5-letter word!")

    while attempts > 0:
        guess = input(f"\nYou have {attempts} attempts left. Enter your guess: ").strip().lower()
        if len(guess) != 5 or guess not in words:
            print("Invalid guess. Please enter a 5-letter word from the word list.")
            continue
        
        feedback = get_feedback(guess, answer)
        print(f"Progress: {feedback}")

        if guess == answer:
            print("Congratulations! You've guessed the word!" + Style.RESET_ALL)
            return
        
        attempts -= 1
    
    print(f"Sorry, you've run out of attempts. The word was '{answer}'." + Style.RESET_ALL)

# Directly call the function
wordle()

