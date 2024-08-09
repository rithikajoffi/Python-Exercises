# Exercise Name:
# 	04-List-Occurence-Counter
# Description:
# 	Display all duplicate items from a list
# Given:
# 	sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
# Return:
# 	[20, 60, 30]
# Hint: 
# 	Count occurence of each item in the list and print items occuring more than once.

num = int(input(" Enter the number of items to be added to the list : "))

newlist = []
duplist = []

for i in range(num):
    print(f" Enter item {i+1} : ", end="")
    newlist.append(int(input()))

print(" The given list is :", end="")
print(newlist)

print(" The duplicates in the list are : ", end="")
i = 0
while i < num :
    count = 0
    j = 0
    for j in range(num) :
        if newlist[i] == newlist[j] :
            count += 1
    if count > 1 :
        if newlist[i] not in duplist :
            duplist.append(newlist[i])
    i += 1
print(duplist)