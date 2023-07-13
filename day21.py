# cook your dish here
T = int(input())  

for _ in range(T):
    salary = int(input())  

    if salary < 1500:
        hra = 0.1 * salary
        da = 0.9 * salary
    else:
        hra = 500
        da = 0.98 * salary

    gross_salary = salary + hra + da
    print("{:.2f}".format(gross_salary))
