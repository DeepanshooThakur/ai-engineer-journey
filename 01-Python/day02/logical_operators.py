age=int(input("Enter your Age"))
has_id = input("Do you have id(yes/NO):")
if age>= 18 and has_id.lower()=="yes":
    print("You are allowed")
else:
    print("You are not allowed")    