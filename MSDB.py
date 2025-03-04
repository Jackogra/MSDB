# Task description available in README.md file

# Class creating instances of Movies
class Movie:
    def __init__(self, title, release_year, genre):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.play_count = 0

    def play(self):
        self.play_count += 1

    def __str__(self):
        return f"{self.title} ({self.release_year})"
    
    def __gt__(self, other):
        return self.title > other.title
        

class Series(Movie):
    def __init__(self, title, release_year, genre, season, episode):
        super().__init__(title, release_year, genre)
        self.season = format(season, "02d")
        self.episode = format(episode, "02d")
        self.play_count = 0

    def play(self):
        self.play_count += 1

    def __str__(self):
        return f"{self.title} S{self.season}E{self.episode}"


media_library = []

media_library.append(Movie("The Shawshank Redemption", 1994, "Drama"))
media_library.append(Movie("The Dark Knight", 2008, "Action"))
media_library.append(Movie("Forrest Gump", 1994, "Drama"))
media_library.append(Movie("The Matrix", 1999, "Sci-Fi"))
media_library.append(Movie("Interstellar", 2014, "Sci-Fi"))
media_library.append(Movie("The Godfather", 1972, "Comedy"))
media_library.append(Movie("Toy Story", 1995, "Animation"))
media_library.append(Series("The Office", 2005, "Comedy", 2, 3))
media_library.append(Series("Friends", 1994, "Comedy", 5, 10))
media_library.append(Series("How I Met Your Mother", 2005, "Comedy", 7, 12))
media_library.append(Series("Brooklyn Nine-Nine", 2013, "Comedy", 5, 1))
media_library.append(Series("Miami Vice", 1984, "Crime", 3, 9))
media_library.append(Series("Knight Rider", 1982, "Action", 2, 3))
media_library.append(Series("Scooby Doo", 1982, "Cartoon", 3, 8))


if __name__ == "__main__":

    def get_movies():
        movies = [title for title in media_library if not(isinstance(title, Series))]
        return sorted(movies)

    def get_series():   # function to return movies sorted by title
        series = [title for title in media_library if isinstance(title, Series)]
        return sorted(series)
            

    
new = get_series()
for i in new:
    print(i)
