n = int(input())
i = 1
if n == 1:
    print("YES")
    exit()
while i < n:
    i *= 2
if i == n:
    print("YES")
    exit()
print("NO")