class Episode:
    def __init__(self, id, title, season, number, rating):
        self.season = season
        self.title = title
        self.number = number
        self.id = id
        self.rating = rating

    def __repr__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.season == other.season and self.number == other.number

    def __lt__(self, other):
        return self.season < other.season or (self.season == other.season and self.number < other.number)