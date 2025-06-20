rows = int(input("Please enter the number of rows you want: "))
for i in range(1, rows + 1):
    spaces = rows - i
    stars = i
    print(' ' * spaces + '*' * stars)
