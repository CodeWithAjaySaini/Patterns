# pattern_1.py
# for i in range(0, 6):
#     print("*"*i)


for raw in range(4):
    for col in range(raw+1):
        print("*", end="")
    print()
