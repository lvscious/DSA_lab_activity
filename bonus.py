# Bonus
weight = float(input("Weight (lbs): "))  
destination = input("Destination (domestic/international): ").lower()  
membership = input("Membership (standard/premium): ").lower() 

# Initialize the base cost
cost = 10.0 
details = "Base $10"  

# Check for overweight surcharge
if weight > 20:
    cost += 5  
    details += " + Overweight $5"  

# logical operators
if membership == "premium":
    if destination == "international":
        details += ", International fee waived"  
    cost *= 0.8  
    details += ", Premium 20% discount applied"
elif destination == "international":
    cost *= 2 
    details += ", International fee applied"

# Print the final shipping cost with details
print(f"Final Shipping Cost: ${cost:.2f}")
print(f"(Details: {details}.)")
