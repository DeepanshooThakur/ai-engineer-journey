cart=[]
while True:
    print("\n========Shopping Cart======")
    print("1.Add item")
    print("2.Remove item")
    print("3.View cart")
    print("4.Exit")

    choose=input("Please select an option:")
    if choose=="1":
        item=input("choose an item:")
        cart.append(item)
        print(item,"Added to the cart")
    elif choose=="2":
        item=input("Choose an item to remove:")
        if item in cart:
            cart.remove(item)
            print(item, "has been removed")
        else:
            print("Item not found")
    elif choose=="3":
        if len(cart)==0:
            print("Cart is empty")
        else:
            print("\n Your cart")
            for i in range(len(cart)):
                print(i+1,".",cart[i],sep="")
    elif choose=="4":
        print("Thank you!")
        break
    else: 
        print("Invalid option")               