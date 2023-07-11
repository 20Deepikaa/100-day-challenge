n=int(input())
for i in range(n):
    n,m=map(int, input().split())
    if(n<=m):
        print(n)
    elif (m==0):
        z=n*2
        print(z)
    else:
        A=n-m
        B=A+n
        print (B)