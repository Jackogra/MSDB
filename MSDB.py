# Task description available in README.md file
import random
import datetime


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

    def __str__(self):
        return f"{self.title} S{self.season}E{self.episode}"


def get_media(media_library, media_type):     # function that filter Movies or Series
    get_media = [item for item in media_library if (type(item) == Series) == media_type]
    return get_media


def get_movies(media_library):     # function to return movies sorted by title
    return sorted(get_media(media_library, media_type=False))


def get_series(media_library):     # function to return series sorted by title
    return sorted(get_media(media_library, media_type=True))


def search(title, media_library):     # function to search if given title is to be found in the media_library
    search_result = [item for item in media_library if item.title.lower() == title.lower()]
    if search_result:
        print("Found the following matches: ")
        for item in search_result:
            print(item)
    else:
        print("No matches found.")


def generate_views(media_library):     # function to generate random play count on a random production in a database
    production = random.choice(media_library)
    production.play_count += random.randint(1, 100)


def run_generate_views(media_library):     # function to run generate_views() 10 times
    run_generate_views_item = [generate_views(media_library) for title in range(10)]


def top_titles(num, media_library):     # function to return top watched titles in the library
    # no_of_top_productions = int(input("How many top movies you want to check?: "))
    sorted_top_titles = sorted(media_library, key=lambda item: item.play_count, reverse=True)
    return sorted_top_titles[:num]

media_library = []

if __name__ == "__main__":
    print("Media Library")
    media_library = [
        Movie("The Shawshank Redemption", 1994, "Drama"),
        Movie("The Dark Knight", 2008, "Action"),
        Movie("Forrest Gump", 1994, "Drama"),
        Movie("The Matrix", 1999, "Sci-Fi"),
        Movie("Interstellar", 2014, "Sci-Fi"),
        Movie("The Godfather", 1972, "Crime"),
        Movie("Toy Story", 1995, "Animation"),
        Movie("Inception", 2010, "Sci-Fi"),
        Movie("Pulp Fiction", 1994, "Crime"),
        Movie("The Lord of the Rings: The Return of the King", 2003, "Fantasy"),
        Movie("Gladiator", 2000, "Action"),
        Movie("The Lion King", 1994, "Animation"),
        Movie("Titanic", 1997, "Romance"),
        Movie("Saving Private Ryan", 1998, "War"),
        Movie("The Green Mile", 1999, "Drama"),
        Movie("The Silence of the Lambs", 1991, "Thriller"),
        Movie("Schindler's List", 1993, "History"),
        Movie("Back to the Future", 1985, "Sci-Fi"),
        Movie("The Departed", 2006, "Crime"),
        Movie("Whiplash", 2014, "Drama"),
        Series("The Office", 2005, "Comedy", 2, 3),
        Series("Friends", 1994, "Comedy", 5, 10),
        Series("How I Met Your Mother", 2005, "Comedy", 7, 12),
        Series("Brooklyn Nine-Nine", 2013, "Comedy", 1, 0),
        Series("Miami Vice", 1984, "Crime", 3, 5),
        Series("Knight Rider", 1982, "Action", 2, 3),
        Series("Scooby Doo", 1982, "Cartoon", 3, 8),
        Series("Breaking Bad", 2008, "Crime, Drama", 6, 18),
        Series("Stranger Things", 2016, "Drama, Fantasy, Horror", 4, 2),
        Series("The Crown", 2016, "Biography, Drama, History", 2, 8),
        Series("The Mandalorian", 2019, "Action, Adventure, Fantasy", 1, 11),
        Series("The Simpsons", 1989, "Animation, Comedy", 33, 15),
        Series("The Witcher", 2019, "Action, Adventure, Drama", 2, 5),
        Series("Westworld", 2016, "Drama, Mystery, Sci-Fi", 4, 14),
        Series("Peaky Blinders", 2013, "Crime, Drama", 6, 4),
        Series("Narcos", 2015, "Biography, Crime, Drama", 2, 12),
        Series("Fargo", 2014, "Crime, Drama, Thriller", 3, 7),
        Series("Sherlock", 2010, "Crime, Drama, Mystery", 3, 10),
        Series("Black Mirror", 2011, "Drama, Sci-Fi, Thriller", 2, 7),
        Series("The Boys", 2019, "Action, Comedy, Crime", 1, 2)
    ]
    run_generate_views(media_library)
    print(f"The most popular movies and series on {datetime.date.today()}:")
    top_titles = top_titles(3, media_library)
    for top_title in top_titles:
        print(top_title)
