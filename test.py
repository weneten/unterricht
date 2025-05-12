eingabe = int(input("Die wievielte Fibonacci Zahl soll berechnet werden:"))
n = eingabe
nx = 3
x = 1
y = x + (x - 1)
z = x + y
while nx <= n:
    if nx >= n:
        print(y)
        break
    else:
        nx += 1
        z = x + y
    if nx >= n:
        print(z)
        break
    else:
        x = y + z
        nx += 1
    if nx >= n:
        print(x)
        break
    else:
        y = z + x
        nx += 1
