# This program simulates a Magic 8-Ball that answers yes-or-no questions.
# It greets the user, reacts to their name length, and gives a random response.

import random

# Prompt the user for their name
name = input("Enter your name: ").strip()

# Check if the user entered a name
if name == "":
    name = "Guest"
    print(f"Welcome, {name}!")
else:
    name = name.title()
    print(f"Welcome, {name}!")

    # Respond based on the length of the name
    if len(name) < 4:
        print("Your name is short and sweet!")
    elif 4 <= len(name) <= 6:
        print("Great name! Balanced and bold.")
    else:
        print("Your name carries power in every letter!")

# Ask the user a yes-or-no question
print("\nWhat is your question?")
question = input("> ")

# List of possible Magic 8-Ball responses
responses = [
    "Yes, definitely.",
    "No, certainly not.",
    "Ask again later.",
    "Outlook not so good.",
    "It is possible."
]

# Select a random response
answer = random.choice(responses)

# Display the Magic 8-Ball response
print("\nMAGIC 8-BALL SAYS:")
print(f"\"{answer}\"")