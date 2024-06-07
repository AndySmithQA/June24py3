#Question 1
# Create two variables, one containing your first name.
first = 'Fred'
# And another containing your last name.
last = 'Bloggs'
# Display them using print.
print(first, last)

# Now transfer these variable values into a list.
names = [first, last]
# Display the list.
print(names)

# Transfer these variable values into a dictionary,
# using keys 'first' and 'last'.
mydict = {'first': first,
          'last': last
    }

# Display the values.
print(mydict['first'], mydict['last'])

#Question 2
var = input("Please enter a value: ")

# Display the value of var in upper case.
print(var.upper())
# Display the number of characters in var.
print(len(var))

#Question 3
a = 6
b = 6

# a)
print(a == b)
# c)
print(a is b)
