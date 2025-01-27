#Question 1
import subprocess
import os
import sys

#(a)
proc = subprocess.run([sys.executable, 'client.py', 'words'])
print('Child exited with', proc.returncode)

#(b)
proc = subprocess.run([sys.executable, 'client.py', 'words'],
             stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if proc.stderr != None:
    print('error:', proc.stderr.decode())

print('output:', proc.stdout.decode())

#Question 2

import mytimer
from multiprocessing import Process


def stem_search(stems, stem_size):
    best_stem = ''
    best_count = 0
    for (stem, count) in stems.items():
        if stem_size == len(stem) and count > best_count:
            best_stem = stem
            best_count = count
    if best_stem:
        print('Most popular stem of size', stem_size, 'is:',
              best_stem, '(occurs', best_count, 'times)')
    return


if __name__ == '__main__':
    mytimer.start_timer()
    stems = {}
    for row in open('words', 'r'):
        for count in range(1, len(row)):
            stem = row[0:count]
            if stem in stems:
                stems[stem] += 1
            else:
                stems[stem] = 1
    mytimer.end_timer('Load')

    # Process the stems.
    mytimer.start_timer()
    n = 30
    processes = []
    for stem_size in range(2, n + 1):
        proc = Process(target=stem_search,
                       args=(stems, stem_size))
        proc.start()
        processes.append(proc)
    for proc in processes:
        proc.join()
        mytimer.end_timer('Process')
