nums = 0
uppers = 0
lowers = 0
symbols = "!£$%^&*()@#~?><,./{;:'[]}"
syms = 0

pw = input("Please enter your password: ")
if len(pw) < 8:
    print("Your password is too short.")
else:
    for char in pw:
        if char.isnumeric():
            nums += 1
        elif char.isupper():
            uppers += 1
        elif char.islower():
            lowers += 1
        elif char in symbols:
            syms += 1
        else:
            print("Your password contains invalid characters.")
            break
if nums == 0:
    print("Your password does not contain any numbers.")
if uppers == 0:
    print("Your password does not contain any uppercase letters.")
if lowers == 0:
    print("Your password does not contain any lowercase letters.")
if syms == 0:
    print("Your password does not contain any symbols.")