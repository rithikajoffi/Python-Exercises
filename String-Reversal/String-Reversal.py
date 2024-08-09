# Exercise Name:
# 	01-String-Reversal
# Description:
# 	Reverse each word of a string.
# Given: 
# 	sentence = "Python is Awesome"
# Return: 
# 	"nohtyP si emosewA"

sentence = str(input( " Enter a sentence : "))
print(" The reverse of the above sentence is : ", end="")
print(sentence[::-1])