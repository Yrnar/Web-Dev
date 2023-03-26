def xor(x, y):
    return x ^ y
arr = list(map(int, input().split()))
print(xor(arr[0], arr[1]))