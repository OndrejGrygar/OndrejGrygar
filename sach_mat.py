def chessboard(n):
    for i in range(n):
        for j in range(n):
            print("#", end=" ") if (j+i)% 2 == 0  else print(".", end=" ")
        print()
chessboard(8)