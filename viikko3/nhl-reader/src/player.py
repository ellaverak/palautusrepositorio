class Player:
    def __init__(self, name, nationality, team, goals, assists):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.goals = goals
        self.assists = assists
        self.points = goals + assists

    def __str__(self):
        return f"{self.name:25} {self.team} {self.goals:2} + {self.assists:2} = {self.points:2}"