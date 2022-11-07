import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_found(self):
        player = self.statistics.search("Semenko")
        self.assertEqual(player, self.statistics._players[0])

    def test_search_not_found(self):
        player = self.statistics.search("Selänne")
        self.assertEqual(player, None)

    def test_team(self):
        team = self.statistics.team("EDM")
        for player in team:
            self.assertEqual(player.team, "EDM")

    def test_top(self):
        sorted = self.statistics.top(2)

        for i in sorted:
            print(i)

        self.assertEqual(sorted[0], self.statistics._players[4])
        self.assertEqual(sorted[1], self.statistics._players[1])
        self.assertEqual(sorted[2], self.statistics._players[3])