class Cricketplayer:
    team_size = 11

    def __init__(self, fname, lname, birth_year):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birth_year


virat = Cricketplayer("virat", "kohli", 1988)
print(virat.first_name)
print(virat.last_name)
print(virat.birth_year)