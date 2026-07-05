Name = input("Please enter your name:")
age = int(input("Please enter your age:"))
print("\n Ticket Checker")
print("welcome",Name)
if age<= 13:
    print("Child Ticket")
elif age<=17:
    print("Teen Ticket")
elif age<=59:
    print("Adult Ticket")
else:
    print("Senior ticket")       