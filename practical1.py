-------------Lab Assignment 1--------

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




------LAB ASSIGNMENT 2------

# Vendor Annual Purchase / Billing Report

# Store vendor details
vendor_name = input("Enter Vendor Name: ")
year_of_association = int(input("Enter Year of Association: "))
contact_number = input("Enter Contact Number: ")
email_id = input("Enter Email ID: ")

# Read monthly purchases
monthly_purchases = []
print("\nEnter monthly purchase amount for 12 months:")
for month in range(1, 13):
    amount = float(input(f"Month {month}: Rs. "))
    monthly_purchases.append(amount)

# Calculate annual purchase
annual_purchase = sum(monthly_purchases)
average_purchase = annual_purchase / 12

# Display Annual Purchase / Billing Report
print("\n========== ANNUAL PURCHASE / BILLING REPORT ==========")
print("Vendor Name        :", vendor_name)
print("Year of Association:", year_of_association)
print("Contact Number     :", contact_number)
print("Email ID           :", email_id)
print("-----------------------------------------------------")
for i, amt in enumerate(monthly_purchases, start=1):
    print(f"Month {i:2d} Purchase : Rs. {amt}")
print("-----------------------------------------------------")
print("Total Annual Purchase : Rs.", annual_purchase)
print("Average Monthly Purchase : Rs.", average_purchase)
print("=====================================================")