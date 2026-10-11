# Author: Lewis Johnson
# Program: Prog Assign_5 - Functions
# Date: oct, 10, 2026
#  https://github.com/lewisjohnson229/Prog-Assign_5---Functions-/blob/main/Prog%20Assign_5%20-%20Functions.py

# Function that calculates the total monthly automobile cost
def calculate_monthly_cost(loan, insurance, gas, oil, tires, maintenance):
    monthly_total = loan + insurance + gas + oil + tires + maintenance
    return monthly_total


# Ask the user to enter each monthly automobile expense
loan = float(input("Enter monthly loan payment: $"))
insurance = float(input("Enter monthly insurance cost: $"))
gas = float(input("Enter monthly gas cost: $"))
oil = float(input("Enter monthly oil cost: $"))
tires = float(input("Enter monthly tire cost: $"))
maintenance = float(input("Enter monthly maintenance cost: $"))

# Call the function and store the returned monthly total
monthly_total = calculate_monthly_cost(
    loan, insurance, gas, oil, tires, maintenance
)

# Calculate the annual cost
annual_total = monthly_total * 12

# Display the results
print(f"\nTotal monthly automobile cost: ${monthly_total:.2f}")
print(f"Total annual automobile cost: ${annual_total:.2f}")
