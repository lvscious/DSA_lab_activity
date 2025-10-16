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
