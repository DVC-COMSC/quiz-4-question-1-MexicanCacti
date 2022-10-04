
# ******************************
# Make your Code
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
i = 0
even_clusters = 0

while i < 10:
    user_input = int(input())
    i += 1
    if(i > 10):
        break
    num1 = user_input
    user_input = int(input())
    i += 1
    num2 = user_input
    if(num1 % 2 == 0 and num2 % 2 == 0 ):
        even_clusters += 1
    while num1 % 2 == 0 and num2 % 2 == 0 and i < 10:
        num1 = num2
        user_input = int(input())
        i += 1
        num2 = user_input
    num1 = num2

print(even_clusters)