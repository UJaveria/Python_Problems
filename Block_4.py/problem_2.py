"""
Add a movie to the end, insert one at position 0, then remove one by name
(.remove())"""

fav_movies = ["12th Fail","Hichki","3 Idiots","Taare Zameen Par","Ferrari Ki Sawaari"]
# Add a movie to the end
app_movie = input("Enter movie you want to append : ")
fav_movies.append(app_movie)
print(fav_movies)

# insert one movie at position 0
insert_movie = input("Enter movie : ")
fav_movies.insert(0,insert_movie)
print(fav_movies)

# Removing by name
remove_movie = input("Enter movie name you want to remove : ")
if remove_movie in fav_movies :
    fav_movies.remove(remove_movie) 
    print("Remove successfully")
else :
    print("Sorry, this name doesn't exist in list")

print(fav_movies)