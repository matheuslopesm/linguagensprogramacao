class Song:
    def __init__(self, title, author, time):
        self.title = title
        self.author = author
        self.time = time

    def showInfo(self):
        return f"{self.title} por {self.author} ({self.time})"
