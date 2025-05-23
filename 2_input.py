# Basic Input
# -----------
name = input("What is your name? ")
print("Hello, " + name + "!")  # String concatenation

# Input with Type Conversion
# -------------------------
age = input("How old are you? ")
age = int(age)  # Convert string to integer
print(f"In 5 years, you will be {age + 5} years old")

# Input with Error Handling
# ------------------------
try:
    temperature = float(input("Enter temperature in Celsius: "))
    fahrenheit = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {fahrenheit:.1f}°F")
except ValueError:
    print("Please enter a valid number!")

# Multiple Inputs
# --------------
# Method 1: Separate inputs
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"Full name: {first_name} {last_name}")

# Method 2: Split input
x, y = input("Enter two numbers (separated by space): ").split()
x, y = int(x), int(y)  # Convert to integers
print(f"Sum: {x + y}")

# Input with Validation
# -------------------
while True:
    password = input("Enter a password (min 8 characters): ")
    if len(password) >= 8:
        print("Password is valid!")
        break
    else:
        print("Password is too short. Try again.")

# Input with Default Values
# -----------------------
color = input("Enter your favorite color (press Enter for default): ").strip()
if not color:  # If empty input
    color = "blue"  # Default value
print(f"Your favorite color is {color}")

# Input with Menu Selection
# -----------------------
print("\nMenu:")
print("1. Option One")
print("2. Option Two")
print("3. Exit")

choice = input("Enter your choice (1-3): ")
if choice == "1":
    print("You selected Option One")
elif choice == "2":
    print("You selected Option Two")
elif choice == "3":
    print("Goodbye!")
else:
    print("Invalid choice!")