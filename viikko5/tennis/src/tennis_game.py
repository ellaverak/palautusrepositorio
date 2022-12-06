class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.score_names = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        self.advantage_score_names = {1: "Advantage player1", -1: "Advantage player2"}

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score+=1
        else:
            self.player2_score+=1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.draw_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.win_or_advantage_score()
        else:
            return self.regular_score()

    def draw_score(self):
        if self.player1_score >= 4:
            return "Deuce"
        else:
            return f"{self.score_names[self.player1_score]}-All"

    def win_or_advantage_score(self):
        score_difference = self.player1_score - self.player2_score
        if score_difference >=2:
            return "Win for player1"
        elif score_difference <=-2:
            return "Win for player2"
        else:
            return self.advantage_score_names[score_difference]

    def regular_score(self):
        return f"{self.score_names[self.player1_score]}-{self.score_names[self.player2_score]}"