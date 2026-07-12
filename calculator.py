print("=" * 35)
print("      SIMPLE PYTHON CALCULATOR")
print("=" * 35)

while True:
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "5":
        print("\nThank you for using the calculator!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice! Please try again.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    if choice == "1":
        print(f"\nResult: {num1} + {num2} = {num1 + num2}")

    elif choice == "2":
        print(f"\nResult: {num1} - {num2} = {num1 - num2}")

    elif choice == "3":
        print(f"\nResult: {num1} × {num2} = {num1 * num2}")

    elif choice == "4":
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            print(f"\nResult: {num1} ÷ {num2} = {num1 / num2}")
