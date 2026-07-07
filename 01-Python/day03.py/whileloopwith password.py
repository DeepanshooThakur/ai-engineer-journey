attempts=0
password=0
while password!=12345 and attempts<3:
    password=int(input("Please enter the password:"))
    attempts+=1
    if password!=12345 and  attempts<3:
     print("Wrong password",3- attempts,"attemts remaing")
    elif password == 12345:
     print('Welcome')
    else:
      print("too many attempts")            