# Hangman-CLI
# Description:
# 	Create a hangman CLI game
# Rough game logic:
# 	1. Pick a random word. (Initially just use a hardcoded word like 'watermelon'. Random selection can be done later.)
# 	2. Initialize Guess Count to 6
# 	3. Show one underscore for each character in the word. For example, in case of 'watermelon', show 10 underscores like: _ _ _ _ _ _ _ _ _ _ 
# 	4. Prompt user to input their guess
# 		- Show a sorted list of already guessed characters
# 		- Guess should be ONE character from the alphabet
# 		- Guessed character should be new and not have been previously guessed
# 	5. Check if that character exists in the selected word
# 		a. If the character exists, reveal the character in its position. 
# 		   For example, in case of 'watermelon' and user guessed 'e', show: _ _ _ e _ _ e _ _ _
# 		b. If the character does not exist in the selected word, show warning and decrement Guess Count by one
# 	6. If the Guess Count
# 		a. is greater than zero, loop and take another input
# 		b. becomes zero before guessing all the characters in the word, Game Over.
# For improvement:
# 	https://random-word-api.herokuapp.com/word
    
    
import requests

response = requests.get("https://random-word-api.herokuapp.com/word")
if response.status_code == 200:
    data = response.json()

    if isinstance(data, list) and len(data) > 0:
        word = data[0]
    else:
        print("Unexpected response format.")
        word = "default"
else:
    print("Failed to retrieve a word. Please check your internet connection or the API status.")
    word = "default"
    
print("\n\n\n\nHANGMAN!!")
print("!!Guess should be ONE character from the alphabet!!")
num = len(word)
word_guessed = ['_'] * len(word)
count = 6

print("Word to be guessed: ", end="")
for i in range(num):
    print(word_guessed[i], end=" ")
print("\nChances left: " + str(count))

guessed_letters = []

def word_guess(guessed_letters):
    global count
    print("\n\nGuessed letters are: " + str(guessed_letters))
    letter = input("Guess a letter: ")
    
    if letter not in guessed_letters:
        guessed_letters.append(letter)
        
        flag = 0
        right_guess = 0
        for i in range(num):
            if letter == word[i]:
                flag = 1
                right_guess = 1
                word_guessed[i] = letter
        if right_guess == 1:
            print(":) Right guess")
        if flag == 0:
            count -= 1
            print(":( Wrong guess")
        print("The word now is: ", end="")
        for i in range(num):
            print(word_guessed[i], end=" ")
        print("\nChances left: " + str(count)) 
        
    else:
        print("Letter already guessed. TRY ANOTHER LETTER.")
      
while count > 0:
    word_guess(guessed_letters)
    if '_' not in word_guessed:
        print("   :) Congratulations! You've guessed the word!")
        break
else:
    print("   :/ Game Over. The word was: ", word)