def square(n):
    for i in range(n):
        for j in range(n):
            print("#", end=" ") if i < 1 or j < 1 or j == (n-1) or i ==(n-1)  else print(".",end= " ")
        print()
square(8)