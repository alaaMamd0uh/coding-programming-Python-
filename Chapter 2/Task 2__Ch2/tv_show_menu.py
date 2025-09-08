import json

while True :
    print("Menu:")
    print("---[0] TO Stop LOOP---")
    print("[1] Add a TV show")
    print("[2] Remove a TV show")
    print("[3] Search for a TV show")
    print("[4] Show all TV shows")
    print("[5] Close the program")

    with open("movie.json", "r") as db:
        dataFile = json.load(db)

    yourChoice=int(input("enter your choice: "))
    if yourChoice == 0:
        break
    elif yourChoice == 1:

        title = input("enter movie title:")
        year = int(input("enter year:"))
        genre = input("enter genre:")

        movie = {
            "title": title,
            "year": year,
            "genre": genre
        }
        dataFile.append(movie)
        print("movie added successfully")
        with open("movie.json", "w") as db:
            json.dump(dataFile, db, indent=2)
        print("updated TV show database successfully")

    elif yourChoice == 2:
        removeMovie=None
        title = input("Enter the title of the TV show to remove:")
        for movie in dataFile:
            if movie["title"]==title:
                removeMovie=movie
                break
        if removeMovie:
            dataFile.remove(removeMovie)

        with open("movie.json", "w") as db:
            json.dump(dataFile, db, indent=2)
            print("movie removed successfully")

    elif yourChoice == 3:

            searchMovie=input("Enter the title of the TV show to search:")
            for movie in dataFile:
                if movie["title"] == searchMovie:
                    print(movie)
                    break

    elif yourChoice == 4:
            if dataFile:
             print("TV Shows in the database:")
             for movies in dataFile:
                 print(movies)
            else:
                print("NO MOVIE FOUND")

    elif yourChoice == 5:
        print("closing the program.")
        db.close()


    else:
        print("invalid choice\nplease try again")








