size = 10
symbols = ["#"," "]
desk = []
for i in range(1, size + 1):
    line = []

    for j in range(1, size + 1):
        x = (i + j) % len(symbols)
        line.append(symbols[x])
    desk.append(''.join(line))
print('\n'.join(desk))
