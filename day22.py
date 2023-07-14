t=int(input())
while(t):
    t -= 1
    n=int(input())
    line=list(map(int,input().split()))
    line.reverse()
    for i in range(len(line)):
        if line[i]!=0:
            print(n-i-1)
            break
        else:
            pass