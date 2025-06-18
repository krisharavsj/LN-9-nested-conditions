n = float(input("Enter a decimal number: "))
if n == 0:
    print("0")
else:
    res = ""
    while n > 0:
        res = str(n % 2) + res
        n //= 2
    print(f"Binary: {res}")
