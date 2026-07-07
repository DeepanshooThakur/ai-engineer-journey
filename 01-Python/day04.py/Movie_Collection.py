movie=[]
while True:
    print("\n====Movie Collection====")
    print("1.Add Movies")
    print("2.Remove Movies")
    print("3.View Movies")
    print("4.Search Movies")
    print("5.Exit")
    choose=input("Please select an option:")
    if choose=="1":
        item=input("Please enter a name:")
        movie.append(item)
        print("Your movie has been added")
    elif choose=="2":
        item=input("Please enter a name:")
        if item in movie:
            movie.remove(item)
            print("Movie has been removed")
        else:
           print("Movie not in your collection")
    elif choose=="3":
        if  len(movie)==0:
            print("Empty")
        else:
            print("\n Your Movie Collection")
            movie.sort()
            for i in range(len(movie)):
               print(i+1,".",movie[i],sep="",).sort(movie) 

    elif choose=="4":
        item=input("Please enter a name:")
        if item in movie:
            print("Here is your movie:",item)
        else:
            print("You do not have this movie")
    elif choose=="5":
        print("Thank you")
        break
    else:
        print("Invalid attempt")                         


        
    


    


            

        