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


class Series(Movie):
    def __init__(self, title, release_year, genre, season, episode):
        super().__init__(title, release_year, genre)
        self.season = season
        self.episode = episode
        self.play_count = 0

    def play(self):
        self.play_count += 1
