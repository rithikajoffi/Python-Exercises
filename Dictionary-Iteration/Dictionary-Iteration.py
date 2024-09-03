# Exercise Name:
# 	05-Dictionary-Iteration
# Description:
# 	Reverse Dictionary mapping
# Given:
# 	ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
# Return:
# 	{65: 'A', 66: 'B', 67: 'C', 68: 'D'}

my_dict = {}
rev_my_dict = {}

print(" Sample dictionary : {'A': 65, 'B': 66, 'C': 67, 'D': 68}\n")

num = int(input(" Enter the number of entries you want to add : "))

for _ in range(num):
    key = input("\n Enter the key : ")
    value = int(input(" Enter the value : "))
    my_dict[key] = value  
    rev_my_dict[value] = key
    
print("\n The dictionary is : ", my_dict)

print("\n The reverse dictionary is : ", rev_my_dict)