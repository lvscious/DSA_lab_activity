# Task 4
age_input = input("Age: ")
age = int(age_input) 

student_input = input("Is student? (True/False): ")
is_student = student_input.lower() == 'true' 

base_price = 12

if age >= 65:
    discount = 4  # Senior discount
elif age <= 12:
    discount = 3  # Child discount
elif is_student:
    discount = 2  # Student discount
else:
    discount = 0  # No discount

# Calculate the final price
final_price = base_price - discount

# Print the final price
print(f"Your ticket price is ${final_price}.")
