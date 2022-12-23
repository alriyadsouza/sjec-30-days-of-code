n=int(input("Enter the number of triangles: "))
a = []
for j in range(n):
    print("Enter")
    for i in range(3):
        b=int(input())
        a.append(b)
    a.sort()
    small = a[0]
    mid = a[1]
    big = a[2]
    if j % 3 == 0:
        print(">>",small)
    elif j % 3 == 1:
        print(">>",mid)
    else:
        print(">>",big)
    a.clear()
