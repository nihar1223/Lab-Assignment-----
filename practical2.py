
-------------Lab Assignment 1--------

# Input values
voltage = float(input("Enter Voltage (V): "))
resistance = float(input("Enter Resistance (Ohms): "))

# Calculate current
current = voltage / resistance

# Display current
print("Current (I) =", current, "A")

# Determine nature of current
if current < 0.5:
    print("Low current")
elif 0.5 <= current <= 2:
    print("Normal current")
else:
    print("High current")



    --------lab assignment 2------
    # Input values
hardness = int(input("Enter hardness of steel: "))
carbon = float(input("Enter carbon content: "))
tensile = int(input("Enter tensile strength: "))

# Check conditions
cond1 = hardness > 50
cond2 = carbon < 0.7
cond3 = tensile > 5600

# Determine grade
if cond1 and cond2 and cond3:
    grade = 10
elif cond1 and cond2:
    grade = 9
elif cond2 and cond3:
    grade = 8
elif cond1 and cond3:
    grade = 7
elif cond1 or cond2 or cond3:
    grade = 6
else:
    grade = 5

# Output result
print("Grade of the steel is:", grade)