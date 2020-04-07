lc1 = [i * i for i in range(10)]
print(lc1)
lc2 = [(x, y) for x in range(5) for y in range(10)]
print(lc2)
lc3 = [(x, y) for x in range(5) for y in range(10) if (x * x == y)]
print(lc3)
