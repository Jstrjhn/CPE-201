#initialization
company_name = " "
department = " "
employee_code = ""
employee_name = ""
cut_off = " "
pay_period = " "
gross_earning = " "
overtime = " "
absences = " "
honorarium = "0"
tardinness = " "
withholding_tax = "0"
sss_contribution = "0"
philhealth_contribution = "0"
gross_income = "0"
deductions = "0"
net_pay = "0"
pag_ibig_contribution = "100"

#input
company_name = str(input("Enter the employee's company name:"))
department = str(input("Enter the employee's department:"))
employee_code = str(input("Enter the employee code:"))
employee_name = str(input("Enter the employee name:"))
rate_per_hour = float(input("Enter the rate per hour:"))
number_of_hours_per_payday = float(input("Enter the number of hours per payday:"))
number_of_overtime_hours_per_payday = float(input("Enter the number of overtime hours per payday:"))
number_of_absences_hours_per_payday = float(input("Enter the number of absences of hours per payday:"))
number_of_tardiness_hours_per_payday = float(input("Enter the number of tardiness of hours per payday:"))

#Formulas
basic_pay = rate_per_hour *number-of-hours_per_payday
overtime = numeber_of_overtime_hours_per_payday * rate_per_hour
absences = numeber_of_absences_hours_per_payday * rate_per_hour
tardinness = rate_per_hour * number_of_tardiness_hours_per_payday
honorarium = number_of_hours * rate_per_month
gross_earning = basic_pay + overtime + honorarium

#Calculation for SSS Contribution
if 4250 < gross_earning:
    sss_contribution = 180
elif 4250 <= gross_earning < 4749.99:
    sss_contribution = 202.50
elif 4750 <= gross_earning < 5249.99:
    sss_contribution = 225
elif 5250 <= gross_earning < 5749.99:
    sss_contribution = 247.50
elif 5750 <= gross_earning < 6249.99:
    sss_contribution = 270
elif 6250 <= gross_earning < 6749.99:
    sss_contribution = 292.50
elif 6750 <= gross_earning < 7249.99:
    sss_contribution = 315
elif 7250 <= gross_earning < 7749.99:
    sss_contribtution = 337.50
elif 7750  <= gross_earning < 8249.99:
    sss_contribution = 360
elif 8250 <= gross_earning < 8749.99:
    sss_contribution = 382.50
elif 8750 <= gross_earning < 9249.99:
    sss_contribution = 405
elif 9250 <= gross_earning < 9749.99:
    sss_contribution = 427.50
elif 9750 <= gross_earning < 10249.99:
    sss_contribution = 450
elif 10250 <= gross_earning < 10749.99:
    sss_contribution = 472.50
elif 10750 <= gross_earning < 11249.99:
    sss_contribution = 495
elif 11250 <= gross_earning < 11749.99:
    sss_contribution = 517.50
elif 11750 <= gross_earning < 12249.99:
    sss_contribution = 540
elif 12250 <= gross_earning < 12749.99:
    sss_contribution = 562.50
elif 12750 <= gross_earning < 13249.99:
    sss_contribution = 585
elif 13250 <= gross_earning < 13749.99:
    sss_contribution = 607.50
elif 13750 <= gross_earning < 14249.99:
    sss_contribution = 630
elif 14250 <= gross_earning < 14749.99:
    sss_contribution = 652.50
elif 14750 <= gross_earning < 15249.99:
    sss_contribution = 675
elif 15250 <= gross_earning < 15749.99:
    sss_contribution = 697.50
elif 15750 <= gross_earning < 16249.99:
    sss_contribution = 720
elif 16250 <= gross_earning < 16749.99:
    sss_contribution = 742.50
elif 16750 <= gross_earning < 17249.99:
    sss_contribution = 765
elif 17250 <= gross_earning < 17749.99:
    sss_contribution = 787.50
elif 17750 <= gross_earning < 18249.99:
    sss_contribution = 810
elif 18250 <= gross_earning < 18749.99:
    sss_contribution = 832.50
elif 18750 <= gross_earning < 19249.99:
    sss_contribution = 855
elif 19250 <=gross_earning < 19749.99:
    sss_contribution = 877.50
else:
    sss_contribution = 900

#Calculation for PHILHealth
if gross_earning == 10000:
    philhealth_contribution = 500
elif 10000 <= gross_earning < 100000:
    philhealth_contribution = gross_earning * 0.5
elif gross_earning == 100000:
    philhealth_contribution = 5000
else:
    philhealth_contribution = 0

#Calculation for Withholding Tax
if 0 <= gross_earning < 20833:
    withholding_tax = 0.00
elif 20833 <= gross_earning < 33332:
    withholding_tax = 0.15/20833
elif 33333 <= gross_earning < 66666:
    withholding_tax = 1875 + 0.20/33333
elif 66667 <= gross_earning < 166666:
    withholding_tax = 8541.80+ 0.25/66667
elif 166667 <= gross_earning < 666666:
    withholding_tax = 33541.80 + 00.30/166667
else:
    withholding_tax = 183541.80 + 0.35/666667














