print("Welcome to the tip calculator!")

bill = input("What was the total bill?\n$")

tip = input("How much tip would you like to give? 10, 12, or 15?\n")

num_people = input("How many people to split the bill?\n")
tip_decimal = int(tip) / 100
bill_after_tip = float(bill) * (1 + tip_decimal)
per_person = round(bill_after_tip / int(num_people), 2)

print(f"Each person should pay: ${per_person}")