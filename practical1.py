# Employee Salary Calculation Program

# Input employee details
name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
department = input("Enter Department: ")
basic_salary = float(input("Enter Basic Salary: "))

# Salary calculations
da = 0.92 * basic_salary      # 92% of Basic Salary
hra = 0.58 * basic_salary     # 58% of Basic Salary
ta = 0.30 * basic_salary      # 30% of Basic Salary
lic = 500                     # LIC deduction

gross_salary = basic_salary + da + hra + ta
net_salary = gross_salary - lic

# Display salary details
print("\n--- Employee Salary Details ---")
print("Name           :", name)
print("Employee ID    :", emp_id)
print("Department     :", department)
print("Basic Salary   : Rs.", basic_salary)
print("DA             : Rs.", da)
print("HRA            : Rs.", hra)
print("TA             : Rs.", ta)
print("LIC Deduction  : Rs.", lic)
print("Net Salary     : Rs.", net_salary)