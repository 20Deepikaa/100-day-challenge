def goodprogram(N):
    nibbles = (N + 3) // 4
    if nibbles * 4 == N:
        return "Good"
    else:
        return "Not Good"

T = int(input())
for _ in range(T):
    N = int(input())
    result = goodprogram(N)
    print(result)
