N=int(input())
for i in  range(N):
    x=int(input())
    if(x%10==0):
        print(int(x/10))
    elif(x%5==0):
            z=int(x/10)+1
            print(z)
    else:
            print("-1")
                