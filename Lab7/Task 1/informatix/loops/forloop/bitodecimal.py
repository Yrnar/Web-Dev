n = input()
ans = 0
sz = len(n) - 1
for i in range (len(n)):
    ans += (2 ** sz) * int(n[i])
    sz -= 1
print(ans)