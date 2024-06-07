def area(h, l):
    print(f"The area of that rectangle is {h*l} cm2")
    vol = input("Would you like to calculate the volume? ('Y')")
    if vol in ("Y", "y"):
        depth = int(input("Please enter the depth: "))
        volume(h,l,depth)
    return None

def volume(h,l,d):
    print(f"The volume of that shape is {h*l*d} cm3")
    return None

height = int(input("Please enter the height: "))
length = int(input("Please enter the length: "))

area(height,length)
