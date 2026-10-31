# Expense Tracker - Installment 4
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

subtotal = 0.0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")
subtotal += amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")
subtotal += amount2

if amount1 > 100 and amount2 > 100:
    print("  Two big expenses in a row - slow down!")

tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

average = subtotal / 2
tax = subtotal * (tax_percent / 100)
total = subtotal + tax

over_budget = total > budget
left = budget - total
amount_diff = abs(left)

# Summary, Bottom Banner & Footer
print()
print("-" * 40)
print("SUMMARY")
print(f"  - {item1}:\t${amount1}")
print(f"  - {item2}:\t${amount2}")
print(f"Total spent:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent:.1f}%):\t${tax}")
print(f"Grand total:\t${total}")
if over_budget:
    print(f"Over budget by ${amount_diff}!")
elif total > (0.90 * budget):
    print(f"Careful: only ${amount_diff} left.")
else:
    print(f"Within budget. ${amount_diff} left.")
print("-" * 40)
print("Made by: Miguel Inigo P. Frayna | Installment 4")
