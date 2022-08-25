# patterns_7.py
for raw in range(1, 6):
    for space in range(1, 6-raw):
        print(" ", end="")
    for col in range(1, raw+1):
        print("*", end="")
    print()
