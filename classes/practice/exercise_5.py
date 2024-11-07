class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def description(self):
        print(f"{self.title} ({self.year}) by {self.director}")

movie1 = Movie("The Lion King", "Rob Minkoff and Roger Allers", 1994)
movie1.description()