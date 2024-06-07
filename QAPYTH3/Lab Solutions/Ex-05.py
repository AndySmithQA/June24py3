#Question 3

import random

lotto = set()           # Create an empty set.

while len(lotto) < 6:
    num = random.randint(1, 50)
    lotto.add(num)      # Add new number to set.


print("Lottery numbers = ", lotto)

#Question 4

machines = {'user100': 'yogi', 'user1': 'booboo', 'user2': 'rupert', 'user3': 'teddy', 'user4': 'care',
            'user5': 'winnie', 'user6': 'sooty', 'user7': 'padders', 'user8': 'polar', 'user9': 'grizzly',
            'user10': 'baloo', 'user11': 'bungle', 'user12': 'fozzie', 'user13': 'huggy', 'user14': None,
            'user15': 'cinnamon', 'user16': 'greppy'}

machines['user17'] = machines['user16']
del machines['user16']

unallocated = []
for user in ('user4', 'user5', 'user6'):
    unallocated += [machines.pop(user)]


machines['user8'] = [machines['user8'], 'kodiak']


for kv in machines.items():
    print(kv)


print("Unallocated machines: ", sorted(unallocated))

