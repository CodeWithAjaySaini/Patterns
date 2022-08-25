# patterns_11.py
# for raw in range(1, 6):
#     for space in range(raw-1, 0, -1):
#         print(" ", end="")
#     for col in range(6-raw, 0, -1):
#         print('*', end="")
#     print("")


# ----------------------------

for raw in range(6, 0, -1):
    # print(raw)
    for sapce in range(1, 7-raw):
        print(" ", end="")
    for col in range(1, raw+1):
        print("*", end="")
    print("")
