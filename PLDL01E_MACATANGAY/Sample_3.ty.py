# initialize the value of net income, gross income, total deduction, name of employee, pag-ibig contribution
net_income = 0
gross_income = 0
total_deduction = 0
employee_name = " "
pagibig_contribution = 100.00

# input the value of rate per hour, num hours per day, num of days per week, num of week per month, SSS Contribution, PHILHEALTH Contribution, Tax Contribution
employee_name = str(input("Enter employee name:" ))
rate_per_hour = float(input("Enter employee's rate per hour:"))
num_hours_per_day = float(input("Enter employee's hours per day:"))
num_days_per_week =  int(input("Enter employee's days per week:"))
num_weeks_per_month  =  int(input("Enter employee's weeks per month:"))
SSS_contribution = float(input("Enter employee's SSS_contribution:"))
PHILHEALTH_contribution = float(input("Enter employee's Philhealth contribution :"))
tax_contribution = float(input("Enter employee's tax contribution:"))

# Setting the formula for gross income, total deduction, net income
gross_income = rate_per_hour * num_hours_per_day * num_days_per_week * num_weeks_per_month
total_deduction = SSS_contribution + PHILHEALTH_contribution + tax_contribution + pagibig_contribution
net_income = gross_income - total_deduction

# Display the computed value for employee name, net income, gross income, total deduction
print("Employee name:",employee_name)
print("Net Income:",net_income)
print("Gross Income:",gross_income)
print("Total Deduction:",total_deduction)