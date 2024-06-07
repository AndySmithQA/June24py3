#Question 1
def my_func1(val, lista=[]):
    lista.append(val)
    print("value of lista is:", lista)
    return


my_func1(42)
my_func1(37)
my_func1(99)

#Question 2
import re


def prep_row(row):
    row = row.rstrip()
    row = re.sub(r"'", r"''", row)

    # Add quotes around each field
    lrow = []
    for field in row.split(","):
        lrow.append("'" + field + "'")

    return ",".join(lrow)


for row in open("country.txt", "r"):
    print(prep_row(row))

#Question 3
lrow = list((map(lambda f: "'" + f + "'", row.split(','))))
