for row in range(1, 9):
    for col in range(0, 9):
        if col == 0 or col == 10 or (row == col and (col > 0 and col < 10)):
            print("*****", end="")
        else:
            print(end=" ")
    print("*****")
