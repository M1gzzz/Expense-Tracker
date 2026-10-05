# Expense Tracker - Intallment 2
# Miguel Inigo P. Frayna

# Top Banner & Title
print("=" * 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

# Welcome Message
print("\nWelcome! This is your personal expense tracker.\n")

# Main Menu
print("MAIN MENU")
print("\t[1] Add an expense" + " " * 6 + "(coming soon)")
print("\t[2] View all expenses" + " " * 3 + "(coming soon)")
print("\t[3] Show total spent" + " " * 4 + "(coming soon)")
print("\t[4] Exit" + " " * 16 + "(coming soon)")

# User Input
name = input("\nWhat's your name? ")
print(f"Welcome, {name}! Let's log two expenses.\n")
item1 = input("First expense? ")
amount1 = float(input("Amount? "))
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
total = amount1 + amount2
average = total / 2

# Summary, Bottom Banner & Footer
print()
print("-" * 40)
print("SUMMARY")
print(f"  - {item1}:\t${amount1}")
print(f"  - {item2}:\t${amount2}")
print(f"Total spent:\t${total}")
print(f"Average:\t${average}")
print("-" * 40)
print("Made by: Miguel Inigo P. Frayna | Installment 2")
