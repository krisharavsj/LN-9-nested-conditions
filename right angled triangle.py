print ("triangle in a pattern of stars *")
n=int(input("please enter the number of rows"))
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()