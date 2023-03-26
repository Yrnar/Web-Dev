num = input()
ans = ""
for i in range(len(num) - 1, -1, -1):
    ans += num[i]
print(int(ans))