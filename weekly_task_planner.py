# This program creates a weekly task planner by letting the user enter tasks
# and assign one task to each day of the week, then displays the schedule and repeated tasks.

# Define the days of the week as a tuple
days_of_week = (
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
)

# Prompt user to enter tasks
task_input = input("Enter your tasks (comma separated, e.g., laundry, study, groceries): ")

# Convert string to list
task_list = task_input.split(",")

# Clean tasks
cleaned_tasks = []
for task in task_list:
    cleaned_task = task.strip().title()
    if cleaned_task != "":
        cleaned_tasks.append(cleaned_task)

# Display cleaned task list
print("\nYour Task List:")
for task in cleaned_tasks:
    print(f"- {task}")

# List to store (day, task) tuples
weekly_plan = []

# Assign tasks to each day
for day in days_of_week:
    raw_input_task = input(f"\nWhich task will you do on {day}? ").strip()
    formatted_task = raw_input_task.title()

    if formatted_task in cleaned_tasks:
        weekly_plan.append((day, formatted_task))
    else:
        print(f"\"{raw_input_task}\" is not a valid task. Assigned 'Free Day' instead.")
        weekly_plan.append((day, "Free Day"))

# Print weekly plan
print("\nYour Weekly Plan:\n")

for day, task in weekly_plan:
    print(f"{day:<10} → {task}")

# Count repeated tasks
print()

for task in cleaned_tasks:
    count = 0

    for day, assigned_task in weekly_plan:
        if assigned_task == task:
            count += 1

    if count > 1:
        print(f'You scheduled "{task}" {count} time(s).')