n, m = map(int, input().split())
for i in range(n, m):
    if i % 3 == 0:
        print("Foo")7
        pass
    if i % 2 == 0:
        print("Baz")
    else:
        print("Bar")