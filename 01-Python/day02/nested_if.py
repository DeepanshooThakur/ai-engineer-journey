age = int(input("Enter your age:"))
if age >=18:
   has_id = input("Do you have ID(Yes/No):")
   if has_id.lower()=="yes":
    print("Entery Allowed")
   else:
     print("Bring your id")
else:
  print("You are underage")