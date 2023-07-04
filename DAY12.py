T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    valuation_A = A * 10
    valuation_B = B * 5
    if valuation_A > valuation_B:
        print("FIRST")
    elif valuation_A < valuation_B:
        print("SECOND")
    else:
        print("ANY")
