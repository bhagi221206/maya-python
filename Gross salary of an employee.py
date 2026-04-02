basic_salary = float(input())
hra = float(input())
da = float(input())
pf = 0.12 * basic_salary
gross_salary = basic_salary + hra + da + pf
print(f"{pf:.2f}")
print(f"{gross_salary:.2f}")
