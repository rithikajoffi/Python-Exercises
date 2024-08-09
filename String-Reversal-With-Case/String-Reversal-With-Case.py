# Exercise Name:
# 	02-String-Reversal-With-Case
# Description:
# 	Reverse each word of a string without changing upper-case positions.
# Given: 
# 	sentence = "Python is Awesome"
# Return: 
# 	"Nohtyp si Emosewa"

sentence = input("Enter a sentence: ")

def reverse_with_case(word):
    reversed_word = word[::-1]
    result = []
    for i in range(len(word)):
        if word[i].isupper():
            result.append(reversed_word[i].upper())
        else:
            result.append(reversed_word[i].lower())
    reversed_word_with_case = ""
    for char in result:
        reversed_word_with_case += char
    return reversed_word_with_case

words = sentence.split()

reversed_words = []
for word in words:
    reversed_words.append(reverse_with_case(word))

for i in range(len(reversed_words)):
    if i != 0:
        print(" ", end="")
    print(reversed_words[i], end="")

print()