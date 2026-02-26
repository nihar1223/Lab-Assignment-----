# Lab Assignment 1

text = input("Enter a string: ")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
space_count = 0
lowercase_count = 0

for ch in text:
    if ch in vowels:
        vowel_count += 1
    elif ch.isalpha():
        consonant_count += 1
    elif ch == " ":
        space_count += 1

    if ch.islower():
        lowercase_count += 1

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
print("Number of spaces:", space_count)
print("Number of lowercase letters:", lowercase_count)


# Lab Assignment 2

def capitalize_lines():
    lines = input("Enter a sentence: ")
    print(lines.upper())

# Function call
capitalize_lines()