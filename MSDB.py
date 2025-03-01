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


nowy = Movie("The Simpsons", 1998, "Comedy")
print(nowy.__str__())
