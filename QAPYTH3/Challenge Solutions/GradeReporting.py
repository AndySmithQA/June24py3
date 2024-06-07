again = "yes"
while again == "yes":
    score = int(input("Enter a score between 0 and 100: "))
    if score > 100 or score < 0:
        print("That Score was out of bounds")
    else:
        if score > 90:
            print('A*')
        elif score > 80:
            print('A')
        elif score > 70:
            print('B')
        elif score > 60:
            print('C')
        elif score > 50:
            print('D')
        elif score > 40:
            print('E')
        else:
            print('F')

    more = input("Would you like to check another score")
    if more not in ("Y", "yes", "y"):
        again = "no"
print("Thank you - Goodbye")