a = set()
for i in range(1, 31):
    a.add(i)
b = set()
for i in range(28):
    b.add(int(input()))
c = list(a-b)
c.sort()
for i in range(2):
    print(c[i])