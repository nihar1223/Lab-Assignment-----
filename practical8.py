#LAB ASSIGNMENT 1_______________________________________________
# Take file names from user
source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

# Open source file in read mode
with open(source, "r") as f1:
    content = f1.read()

# Convert content to uppercase
upper_content = content.upper()

# Write into destination file
with open(destination, "w") as f2:
    f2.write(upper_content)

print("Content copied in uppercase successfully.")




#LAB ASSIGNMENT 2_______________________________________________
# Program to copy python file without comments

# Take file names from user
source = input("Enter source python file name: ")
destination = input("Enter destination file name: ")

with open(source, "r") as f1, open(destination, "w") as f2:
    
    for line in f1:
        # Remove comments
        if not line.strip().startswith("#"):
            f2.write(line)

# Print both file contents
print("\nSource File Content:")
with open(source, "r") as f:
    print(f.read())

print("\nDestination File Content (Without Comments):")
with open(destination, "r") as f:
    print(f.read())