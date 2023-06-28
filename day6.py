
T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    max = M * K
    if max >= N:
        print("Yes")
    else:
        print("No")
