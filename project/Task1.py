"""
Beckett Pizza Plaza - 4 for 3 Offer Calculator

This program asks the user to enter the prices of four pizzas.
The cheapest pizza is free. The program then calculates:
- The total price to pay
- The discount percentage achieved

Invalid inputs (non-numeric, zero, negative) are rejected.
"""

print("Beckett Pizza Plaza 4-for-3 Offer")
print("=================================\n")

prices = []

pizza_number = 1

while pizza_number <= 4:
    user_input = input(f"Enter Price of Pizza #{pizza_number}: ")

    try:
        price = float(user_input)

        if price <= 0:
            print("Please enter a valid price!")
            continue

        prices.append(price)
        pizza_number += 1

    except ValueError:
        print("Please enter a valid price!")

# Calculate original total (without discount)
original_total = sum(prices)

# Find cheapest pizza (free one)
cheapest = min(prices)

# Calculate discounted total
final_total = original_total - cheapest

# Calculate discount percentage
discount_percentage = (cheapest / original_total) * 100

# Output result formatted to 2 decimal places
print(f"\nOrder Total is £{final_total:.2f}, a fabulous discount of {discount_percentage:.0f}%!")
