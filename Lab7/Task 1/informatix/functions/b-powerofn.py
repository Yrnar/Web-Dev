def power(a , n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)
    
arr = list(map(int, input().split()))
print(power(arr[0], arr[1]))