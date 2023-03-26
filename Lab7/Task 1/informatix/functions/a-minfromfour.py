def minFromFour(a, b, c, d):
    mini = a
    if mini > b:
        mini = b
    if mini > c:
        mini = c
    if mini > d:
        mini = d
    return mini
arr = list(map(int, input().split()))
print(minFromFour(arr[0],arr[1],arr[2],arr[3]))