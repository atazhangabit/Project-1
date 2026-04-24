print("=== Multiplication Table Program ===")

while True:
    print("\nMenu:")
    print("1 - Show multiplication table for one number")
    print("2 - Show multiplication tables from 1 to 10")
    print("3 - Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        try:
            num = int(input("Enter a number: "))
            print("\nMultiplication table for", num)
            print("----------------------------")

            for i in range(1, 11):
                print(num, "x", i, "=", num * i)

        except ValueError:
            print("Error: please enter a whole number.")

    elif choice == "2":
        print("\nMultiplication tables from 1 to 10")
        print("----------------------------------")

        for num in range(1, 11):
            print("\nTable for", num)
            for i in range(1, 11):
                print(num, "x", i, "=", num * i)

    elif choice == "3":
        print("Program finished.")
        break

    else:
        print("Error: please choose 1, 2, or 3.")
