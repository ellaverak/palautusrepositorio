def sort_by(player, category):
    if category == 1:
        return player.points
    elif category == 2:
        return player.goals
    else:
        return player.assists

class Statistics:
    def __init__(self, reader):
        self.reader = reader

        self._players = self.reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, category=1):
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=lambda player: sort_by(player, category)
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result

