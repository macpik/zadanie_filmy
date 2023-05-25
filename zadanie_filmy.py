import random
from datetime import date

today = date.today()
d1 = today.strftime("%d/%m/%Y")

class MovieLibrary:
    def __init__(self, title, year, genre, plays):
        self.title = title
        self.year = year
        self.genre = genre
        self.plays = plays
        self._current_plays = 0

    def __repr__(self):
        return f'{self.title} {self.year}'
    
    def get_back(self):
        return f'{self.title} {self.year}'

class SeriesLibrary(MovieLibrary):
    def __init__(self, episod_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episod_number = episod_number
        self.season_number = season_number

    def __repr__(self):
        return f'{self.title} {self.season_number}{self.episod_number}'
    
    def get_back(self):
        return f'{self.title} {self.season_number}{self.episod_number}'

    @property
    def current_plays(self):
        return self._current_plays

    @current_plays.setter
    def current_plays(self):
        self._current_plays += 1

movie_1 = MovieLibrary(title='Pulp Fiction', year=1994, genre='Drama', plays=0)
movie_2 = MovieLibrary(title='Inception', year=2010, genre='Action', plays=0)
series_1 = SeriesLibrary(title="The Simpsons", year=1989, genre="Comedy", plays=0,season_number="S01", episod_number="E01")
series_2 = SeriesLibrary(title="The Sopranos", year=1999, genre="Drama", plays=0,season_number="S03", episod_number="E02")

library = [movie_1, movie_2, series_1, series_2]


def get_movies():
    movie_library = []
    for x in library:
         if type(x) == MovieLibrary:
            movie_library.append(x)
    return sorted(movie_library, key=lambda movie: movie.title)
    

def get_series():
    searies_library = []
    for x in library:
        if type(x) == SeriesLibrary:
            searies_library.append(x)
    return sorted(searies_library, key=lambda movie: movie.title)

def search(search_title):
    for movie in library:
        if search_title == movie.title:
            return movie
    return None

def generate_views(): 
    movie = random.choice(library)
    movie.plays += random.randint(1, 100)

def genera_views_10():
     for x in range(0,11):
         generate_views()

genera_views_10()

def top_titles():
    top_titles_library = []
    for movies in library:
        if movies.plays > 20:
            top_titles_library.append(movies)
    return sorted(top_titles_library, key=lambda x:x.plays, reverse=True)[:3]


print("Biblioteka filmów:", library)


print("Najpopularniejsze filmy i seriale dnia",d1,":")
topka = top_titles()
for x in topka:
    print(x.title, "obejrzenia:", x.plays)

#dla commita
