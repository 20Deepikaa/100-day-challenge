
def qualify(X, A, B):
    score = A + (B * 2)
    if score >= X:
        return "Qualify"
    else:
        return "NotQualify"
T = int(input())
for _ in range(T):
    X, A, B = map(int, input().split())
    result = qualify(X, A, B)
    print(result)
