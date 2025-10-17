# Task 1: Basic Calculator
task_1 = "Task 1: Basic Calculator"
print(task_1)

# Step 1: Assigning two different value
a = 12 
b = 10

# Step 2: Calculate and print the results of the operations

# Addition
addition_result = a + b
print("Addition:", addition_result)

# Subtraction
subtraction_result = a - b
print("Subtraction:", subtraction_result) 

# Multiplication
multiplication_result = a * b
print("Multiplication:", multiplication_result)

# Floating-Point Division
floating_division_result = a / b
print("Floating-Point Division:", floating_division_result)   

# Integer Division
integer_division_result = a // b
print("Integer Division:", integer_division_result)

# Modulus
modulus_result = a % b
print("Modulus:", modulus_result) 

# Exponentiation 
exponentiation_result = a ** b
print("Exponentiation:", exponentiation_result)

# Task 2: Order Operations
task_2 = "\nTask 2: Order Operation"
print(task_2)

# Result 1
result1 = 5 + 3 * 2 ** 2
print("Result 1 (Predicted: 17):", result1)  

# Result 2
result2 = (5 + 3) * 2 ** 2
print("Result 2 (Predicted: 32):", result2)  

# Result 3
result3 = 10 % 3 + 5 * 2
print("Result 3 (Predicted: 11):", result3)  

#Task 3: Unit Conversion
task_3 = "\nTask 3: Unit Conversion"
print(task_3)
# Prompt the user to enter a number of inches
user_input = input("Enter the number of inches: ")

# Convert the input to an integer
total_inches = int(user_input)

# Calculate feet and remaining inches
feet = total_inches // 12 
remaining_inches = total_inches % 12  

# Determine the correct word forms for feet and inches
feet_word = "foot" if feet == 1 else "feet"
inches_word = "inch" if remaining_inches == 1  else "inches"

# Print the result 
print(f"{total_inches} inches is equal to {feet} {feet_word} and {remaining_inches} {inches_word}.")

