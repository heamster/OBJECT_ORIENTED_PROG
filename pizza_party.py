# This program helps a pizza shop calculate how many pizzas to order and the
# total cost for a pizza party, based on fixed assumptions about slices, eating
# habits, and pizza price.

import datetime
import math

# Store the assumptions used for all calculations in this program.
SLICES_PER_PIZZA = 8
SLICES_PER_PERSON = 3
PRICE_PER_PIZZA = 12.50

# Ask for the customer's name and the number of attendees.
raw_name = input("What is the name of the person placing the order? ")
people = int(input("How many people are attending the party? "))

# Display the assumptions that will be used to calculate the order.
print(
    f"\nAssumptions: Each pizza has {SLICES_PER_PIZZA} slices, "
    f"each person eats {SLICES_PER_PERSON} slices, "
    f"and each pizza costs ${PRICE_PER_PIZZA:.2f}.\n"
)

# Format the name with the first letter uppercase and the rest lowercase.
name = raw_name.capitalize()

# Get today's date and format it in a user-friendly way.
today = datetime.date.today()
formatted_date = today.strftime("%m/%d/%Y")

# Calculate total slices needed, pizzas required, and total cost.
total_slices = people * SLICES_PER_PERSON
pizzas_needed = math.ceil(total_slices / SLICES_PER_PIZZA)
total_cost = pizzas_needed * PRICE_PER_PIZZA

# Count the number of letters in the name (excluding spaces).
letters_in_name = len(raw_name.replace(" ", ""))

# Display results using f-strings for all output.
print(f"Hello, {name}!")
print(f"Order placed on: {formatted_date}")
print(f"Total slices to be eaten: {total_slices}")
print(f"Whole pizzas needed: {pizzas_needed}")
print(f"Total amount due: ${total_cost:.2f}")
print(f"Hey, did you know that you have {letters_in_name} letters in your name?")