while True:
    print("\nEnter 'q' to quit.")

    number1 = input("Enter the first number: ")

    if number1.lower() == 'q':
        break

    number2 = input("Enter the second number: ")

    if number2.lower() == 'q':
        break

    try:
        number1 = int(number1)
        number2 = int(number2)

        result = number1 + number2

    except ValueError:
        print("Sorry, please enter numbers only!")
        continue

    else:
        print(f"The result is: {result}")
