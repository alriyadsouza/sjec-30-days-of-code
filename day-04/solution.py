n, m = map(int, input().split())
if (m % 3 == 0 and n % 3 == 0 or m % 3 ==0 and n % 2 == 0 or m % 2 == 0 and n % 3 == 0):
    print("YES")
else:
    print("NO")