class Movie:
    def __init__(self, title: str, director, year, genre, duration):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
        self.duration = duration

    def __str__(self):
        return f"{self.title} ({self.year}), directed by {self.director}, {self.genre}, {self.duration} mins"
    
inception = Movie("Inception", "Christopher Nolan", 2010, "Sci-Fi", 148)
print(inception)

# Define the __str__ method in the following format:
# "Inception (2010), directed by Christopher Nolan, Sci-Fi, 148 mins"

