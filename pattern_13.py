# pattern_13.py
for raw in range(6, 0, -1):
    for space in range(6-raw, 0, -1):
        print(" ", end="")
    for col in range(1, (2*raw-1)+1):
        print("*", end="")
    print('')
