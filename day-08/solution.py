n, m = map(int, input().split())
lis,a,b=[],0,0
for i in range (n, m + 1):  
    if i > 1:  
        for j in range (2, i):  
            if (i % j) == 0:  
                break  
        else:  
            lis.append(i)
for k in range(len(lis)-1):
    sum=0
    if (k+1)<(len(lis)):
        a,b=lis[k],lis[k+1]
    while (a)<(b-1):
        sum+=1
        a+=1
    print(lis[k],'-',b,':',sum)