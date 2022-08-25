# pattern_12.py
for raw in range(1, 6):
    for space in range(6-raw, 0, -1):
        print(' ', end="")
    for col in range(1, (2*raw-1)+1):
        print('*', end="")
    print('')
