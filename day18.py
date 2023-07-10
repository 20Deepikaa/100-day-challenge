def calculate_total_time(X, Y):
    T1 = Y / 2
    T2 = X - Y
    total_time = T1 + T2
    return int(total_time)
X, Y = map(int, input().split())
total_time = calculate_total_time(X, Y)
print(total_time)
