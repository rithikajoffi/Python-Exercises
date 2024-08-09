# Exercise Name:
# 	06-Pattern-Fun
# Description:
# 	Prompt for row count and print a number pattern using that value
# Given:
# 	row_count = 5
# Return:
# 	1 1 1 1 1 
# 	2 2 2 2 
# 	3 3 3 
# 	4 4 
# 	5

num = int(input("Enter row count : "))
display = num
for i in range(1, num+1) :
    for j in range(display+1, 1, -1) :
        print(i, end = " ")
    display-=1
    print("")