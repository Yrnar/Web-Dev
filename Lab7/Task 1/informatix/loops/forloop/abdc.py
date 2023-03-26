n = int(input())
m = int(input())
c = int(input())
d = int(input())

for i in range(n, m + 1):
    if(i % d == c):print(i, end=" ")