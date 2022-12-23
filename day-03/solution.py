n=int(input("Enter the number of integers: "))
lis = []
avg=0.0
print("Enter")
for j in range(n):   
    b=int(input())
    lis.append(b)
    avg+=b
avg=avg/n
print(avg)
for i in lis:
    if i>=avg:
        print(i,end=", ")