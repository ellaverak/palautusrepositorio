class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = []
        for player in self.reader.players:
            if str(player.nationality) == nationality:
                players.append(player)

        players.sort(key=lambda player: player.points, reverse=True)

        return players