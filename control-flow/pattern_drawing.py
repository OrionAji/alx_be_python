user = int(input("Enter the size of the pattern: "))

while user > 0:
    for i in range(user):          # rows
        for j in range(user):      # columns
            print("*", end="")     
        print()                    # move to next line
    break
