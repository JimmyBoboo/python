filmer =  [
        {"name": "inception", "year": "2010", "rating": 8.7},
        {"name": "Inside Out", "year": "2015", "rating": 8.1},
        {"name": "Con Air", "year": "1997", "rating": 6.9 }
          ]


for film in filmer:
    print(film.get("name") + " - " + film.get("year") + " - " + film.get("rating"))
    

