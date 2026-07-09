try:
    age_input = input("Enter your age: ")
    age_next_year = int(age_input) + 1
    print(f"Next year you will be {age_next_year}.")
except ValueError:
    print("Please enter a valid number.")
