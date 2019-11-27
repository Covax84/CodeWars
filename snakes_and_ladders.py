class SnakesLadders:
    """ Snakes and ladders game.
        https://www.codewars.com/kata/587136ba2eefcb92a9000027
    """
    snl_map = {2: 38, 7: 14, 8: 31, 15: 26, 16: 6, 21: 42, 28: 84,
               36: 44, 46: 25, 49: 11, 51: 67, 62: 19, 64: 60, 71: 91,
               74: 53, 78: 98, 87: 94, 89: 68, 92: 88, 95: 75, 99: 80}

    def __init__(self, player_1_pos=0, player_2_pos=0, turn=1, game_over=False):
        self.player_1_pos = player_1_pos
        self.player_2_pos = player_2_pos
        self.turn = turn
        self.game_over = game_over

    def play(self, die1, die2):
        if not self.game_over:
            position = (self.player_1_pos if self.turn == 1 else self.player_2_pos) + die1 + die2

            if position > 100:
                position = 100 + (100 - position)
            if position == 100:
                self.game_over = True
                return 'Player ' + str(self.turn) + ' Wins!'

            if self.turn == 1:
                self.player_1_pos = self.snl_map.get(position, position)
            elif self.turn == 2:
                self.player_2_pos = self.snl_map.get(position, position)

            answer = 'Player ' + str(self.turn) + ' is on square ' + str(self.snl_map.get(position, position))

            if die1 != die2:
                self.turn = 1 if self.turn == 2 else 2
            return answer
        return 'Game over!'
