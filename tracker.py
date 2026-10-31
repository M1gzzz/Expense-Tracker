# Expense Tracker - Installment 5
# Miguel Inigo P. Frayna

# Top Banner & Title
print("=" * 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

# Welcome Message
print("\nWelcome! This is your personal expense tracker.\n")

# User Input
name = input("\nWhat's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}!")

subtotal = 0.0
count = 0

# Main Menu
while True:
    print("\nMAIN MENU")
    print("\t[1] Add an expense")
    print("\t[2] View all expenses" + " " * 3 + "(coming soon)")
    print("\t[3] Show total spent")
    print("\t[4] Exit")

    choice = input("Choose 1-4: ")

    if choice == '1':
        amount = float(input("Amount? "))
        subtotal += amount
        count += 1

        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")
    
    elif choice == '2':
        print("  Coming soon: the tracker can't remember each item yet.")

    elif choice == '3':
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        left = budget - total
        amount_diff = abs(left)

        # Summary, Bottom Banner & Footer
        print("-" * 40)
        print("SUMMARY")
        print(f"Expenses:\t{count}")    
        print(f"Subtotal:\t${subtotal}")
        print(f"Tax ({tax_percent:.1f}%):\t${tax}")
        print(f"Grand total:\t${total}")

        if total > budget:
                print(f"Over budget by ${amount_diff}!")
        elif total > (0.90 * budget):
            print(f"Careful: only ${amount_diff} left.")
        else:
            print(f"Within budget. ${amount_diff} left.")
        print("-" * 40)

    elif choice == '4':
        print(f"Goodbye, {name}!")
        print("-" * 40)
        print("Made by: Miguel Inigo P. Frayna | Installment 5")
        break

    else:
        print(" Please choose 1, 2, 3 or 4.")