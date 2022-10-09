i = 1
even_clusters = 0
cluster = False

user_input = int(input())
num1 = user_input
while i < 10:
    user_input = int(input())
    i += 1
    num2 = user_input
    if cluster == False and num1 % 2 == 0 and num2 % 2 == 0:
        even_clusters += 1
        cluster = True
        num1 = num2  # redundant
    elif num1 % 2 == 0 and num2 % 2 == 0:
        num1 = num2  # redundant
    else:
        cluster = False
        num1 = num2  # redundant
print(even_clusters)
