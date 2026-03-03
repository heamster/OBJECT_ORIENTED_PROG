# This program allows a user to track a daily habit over a chosen period of time.
# It collects user input, tracks completion, and displays a summary at the end.

from datetime import date, timedelta


# This loop allows the user to track multiple habits if they choose.
while True:
    # Ask the user for their name.
    name = input("Enter your name: ").strip()

    # Ask the user for the starting date information.
    year = int(input("Enter the starting year: "))
    month = int(input("Enter the starting month: "))
    day = int(input("Enter the starting day: "))

    # Create a date object using the provided year, month, and day.
    start_date = date(year, month, day)

    # Display the starting date in YYYY-MM-DD format.
    print(f"You entered as your starting date: {start_date}")

    # Ask how many days the user wants to track.
    total_days = int(input("How many days are you tracking? "))

    # Ask what habit they want to track.
    habit = input(
        "What habit do you want to track? For example, study, exercise, etc.: "
    ).strip()

    # Initialize a counter to track successful days.
    success_count = 0

    # Loop through each day in the tracking period.
    for day_number in range(1, total_days + 1):
        response = input(
            f"Did you {habit} on day {day_number}? "
            "Answer 'yes' or 'no': "
        ).strip().lower()

        # If the user answered 'yes', increase the success counter.
        if response == "yes":
            success_count += 1

    # Calculate the ending date of the tracking period.
    end_date = start_date + timedelta(days=total_days)

    # Calculate the success rate as a percentage.
    success_rate = (success_count / total_days) * 100

    # Calculate how many days ago the tracking period ended.
    today = date.today()
    days_ago = (today - end_date).days

    # Display the summary of the tracking period.
    print("--------Summary--------")
    print(f"Habit tracker for {name.title()}:")
    print(f"Habit: {habit.upper()}")
    print(
        f"Tracking period: {start_date.strftime('%B %d, %Y')} "
        f"to {end_date.strftime('%B %d, %Y')}"
    )
    print(f"Completed {success_count} out of {total_days} days.")
    print(f"Success rate: {success_rate:.2f}%")
    print(f"Your tracking ended {days_ago} days ago.")

    # Ask if the user wants to track another habit.
    again = input(
        "Would you like to do another? "
        "Hit 'y' to continue or just hit Enter to quit: "
    ).strip().lower()

    # If the user does not type 'y', end the program.
    if again != "y":
        break