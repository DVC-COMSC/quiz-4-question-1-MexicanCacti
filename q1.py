
# ******************************
# Make your Code
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
i = 0
even_clusters = 0

user_input = int(input())
for i in range(9):
    num1 = user_input
    user_input = int(input())
    num2 = user_input
    if num1 % 2 == 0 and num2 % 2 == 0:
        even_clusters += 1
    num2 = num1

print(f"Output: {even_clusters}")