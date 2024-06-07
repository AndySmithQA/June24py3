#Question 1

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

items = Belgium.split(',')
print('-' * len(Belgium))
print(':' . join(items))
print(int(items[1]) + int(items[3]))


#Question 2

for line in open('messier.txt'):
    if not line: break
    if line.startswith('M'):
        # Slice each field
        mes_num = line[:6].rstrip()
        com_name = line[6:40].rstrip()
        if not com_name: com_name = 'no name'
        obj_type = line[40:64].rstrip()
        const = line[64:].rstrip()
print(f"|{mes_num}|{com_name}|{obj_type}|{const}|")



