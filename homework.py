user_input = input("Enter a number: ")
user_input = user_input.strip()

digit_count = 0

for char in user_input:

    if char.isdigit():
        digit_count += 1

print("Number of digits entered:", digit_count)