# Exercise Name:
# 	03-List-Manipulation
# Description:
# 	Remove items greater than 50 from a list while iterating but without creating a different copy of a list.
# Given:
# 	number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Return:
# 	[10, 20, 30, 40, 50]
# Note:
# 	ID of input and output list should match
	
num = int(input(" Enter the number of items to be added to the list : "))

newlist = []
for i in range(num):
    print(f" Enter item {i+1} : ", end="")
    newlist.append(int(input()))

print(" The current list is :", end="")
print(newlist)

print(" The updated list is :", end="")
i = 0
while i < num :
    if newlist[i] > 50:
        newlist.pop(i)
        num -= 1
    else:
        i += 1
print(newlist)