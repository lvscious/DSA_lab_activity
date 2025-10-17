# Task 4: Price Decider
task_4 = "Task 4: Price Decider"
print(task_4)
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

# Task_05
task_5 = "\nTask 5: Secure System"
print(task_5)
correct_username = "kuromi" 
correct_password = "godiswatchingus" 
correct_2fa_code = "123456" 

# Prompt the user for input
input_username = input("Enter username: ")
input_password = input("Enter password: ")
is_2fa_enabled_input = input("Is 2FA enabled? (y/n): ")
user_is_2fa_enabled = is_2fa_enabled_input.lower() == 'y' 
input_2fa_code = input("Enter 2FA code: ")

# Check the login conditions in a single if statement
if input_username == correct_username and input_password == correct_password and (not user_is_2fa_enabled or input_2fa_code == correct_2fa_code):
    print("Login successful!")
    
else:
    
    
    if input_username != correct_username or input_password != correct_password:
        print("Login failed! Invalid username or password.")
    elif user_is_2fa_enabled and input_2fa_code != correct_2fa_code:
        print("Login failed! Invalid 2FA code.")
