answer = "yes"

while answer == "yes":
    number = int(input("Please enter a number:"))

    for i in range(1, 11):
        print(number, "X", i, "=", number * i)

    answer = input("Do you want another table? (Yes/No): ").lower()

print("Thanks for using my program!")