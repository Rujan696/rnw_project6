def show_choices():
    print("1. Right Triangle Pattern")
    print("2. Pyramid Pattern")
    print("3. Left Triangle Pattern")
    print("4. Numbers (Total, Average, Even Numbers)")

show_choices()

user_choice = input("Enter your choice (1, 2, 3, or 4): ").upper()

if user_choice == "1":
    print("You selected 1. Right Triangle Pattern:")
    rows = int(input("enter your value :"))
    for i in range(1, rows + 1):
        print('* ' * i)

elif user_choice == "2":
    print("You selected 2. Pyramid Pattern:")
    rows = int(input("enter your value :"))
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * (2 * i - 1))

elif user_choice == "3":
    print("You selected 3. Left Triangle Pattern:")
    rows = int(input("enter your value :"))
    for i in range(1, rows + 1):
        print('* ' * i)

elif user_choice == "4":
    print("You selected 4. Numbers Calculation:")
    numbers = range(int(input("enter your value :")) , int(input("enter your valuE :")))
    total = sum(numbers)
    average = total / len(numbers)
    even_numbers = [num for num in numbers if num % 2 == 0]

    print("Total:", total)
    print("Average:", average)
    print("Even Numbers:", even_numbers)

else:
    print("Invalid choice!")