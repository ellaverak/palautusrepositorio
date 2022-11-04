import unittest
from statistics import Statistics
from player import Player
from unittest.mock import patch
import io

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

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search(self, mock_stdout):
        print(self.statistics.search("Semenko"))
        assert mock_stdout.getvalue() == "Semenko EDM 4 + 12 = 16\n"