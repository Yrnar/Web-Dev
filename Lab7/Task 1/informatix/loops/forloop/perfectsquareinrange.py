n = int(input())
m = int(input())

for i in range(n, m + 1):
    if( int(i ** 0.5) * int(i ** 0.5) == i ):
        print(i, end=" ")