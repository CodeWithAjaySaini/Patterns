# patterns_10.py

for raw in range(1, 6):
    for space in range(6-raw, 0, -1):
        print(" ", end="")
    for col in range(raw, 0, -1):
        print(col, end="")
    print("")
