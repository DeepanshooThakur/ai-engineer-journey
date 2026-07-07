movies = []

for i in range(1, 6):
    movie = input(f"Enter movie {i}: ")
    movies.append(movie)
    
print("My favorite Movies")
print("------------------")
for i in range(len(movies)):
    print(i+1,".",movies[i],sep ="")