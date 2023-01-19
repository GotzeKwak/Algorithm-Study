n = int(input())
a = list(map(int, input().split()))

min_ = a[0]
max_ = a[0]

for i in a:
    if min_ > i:
        min_ = i
    if max_ < i:
        max_ = i

print(min_, max_)