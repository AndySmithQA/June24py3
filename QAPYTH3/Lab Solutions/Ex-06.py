#Question 1
import re

infile = open('postcodes.txt', 'r')

valid = 0
invalid = 0

for postcode in infile:
    # Ignore empty lines.
    if postcode.isspace(): continue

    # (a): Remove newlines, tabs and spaces.
    postcode = re.sub('[ \t\n]', '', postcode)

    # (a): Convert to uppercase.
    postcode = postcode.upper()

    # (a): Insert a space before the final digit and 2 letters.
    postcode = re.sub('([0-9][A-Z]{2})$', r' \1', postcode)

    # Print the reformatted postcode.
    print(postcode)

    # (b) Validate the postcode, returning a match object.
    m = re.search(r'^[A-Z]{1,2}[0-9]{1,2}[A-Z]? [0-9][A-Z]{2}$',
                  postcode)
    if m:
        valid += 1
    else:
        invalid += 1

infile.close()

#Question 3
valid_dict = {}
valid = open('validpc.txt', 'r').read().splitlines()
for txt in valid:
    line = txt.split(',')
    valid_dict[line[0]] = line[1]
valid = None
# End of valid_dict initialisation.

# Note the extra parentheses.
m = re.search (r'^([A-Z]{1,2}[0-9]{1,2}[A-Z]?) [0-9][A-Z]{2}$',postcode)
if m:
    valid += 1
    # Part c
    area_district = m.group(1)   # Or alternatively m.groups(1)[0]

    if area_district in valid_dict:
        print(postcode, 'is in', valid_dict[area_district])
    else:
        print(postcode, 'not found')
else:
    invalid += 1

