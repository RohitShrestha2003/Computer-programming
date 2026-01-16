"""
Password Security Verification Program

The program asks the user to enter a password.
If the password is shorter than 9 characters, the program exits.
Otherwise, the user is asked to correctly enter three randomly
chosen characters from the password.
"""

import random

# Ask user for password
password = input("Enter your password: ")

# Check password length
if len(password) < 9:
    print("Password too short.")
    exit()

# Perform three random character checks
checks = 0

while checks < 3:
    # Generate random position (1-based index)
    position = random.randint(1, len(password))

    # Ask user for the character at that position
    guess = input(f"Enter letter at position {position}: ")

    # Check if correct
    if guess == password[position - 1]:
        print("Correct")
        checks += 1
    else:
        print("\nSecurity check failed.")
        exit()

# If all checks passed
print("Security check passed.")
