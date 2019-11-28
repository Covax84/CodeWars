class SnakesLadders:
    """ Snakes and ladders game. Full description at:
        https://www.codewars.com/kata/587136ba2eefcb92a9000027
    """
    # map of the locations of snakes and ladders:
    snakes_and_ladders = {2: 38, 7: 14, 8: 31, 15: 26, 16: 6, 21: 42, 28: 84,
                          36: 44, 46: 25, 49: 11, 51: 67, 62: 19, 64: 60, 71: 91,
                          74: 53, 78: 98, 87: 94, 89: 68, 92: 88, 95: 75, 99: 80}

    def __init__(self):
        self.players_positions = [0, 0]  # index = player, value = player position
        self.game_over = False           # once game is over additional turns are forbidden
        self.current_player = 0          # 0 is for player 1, 1 is for player 2.

    def play(self, die1: int, die2: int):
        if not self.game_over:
            new_position = self.players_positions[self.current_player] + die1 + die2
            # let's check if we hit the snake or the ladder:
            self.players_positions[self.current_player] = self.snakes_and_ladders.get(new_position, new_position)

            if self.players_positions[self.current_player] > 100:   # oh, too much! got to retreat!
                retreat_pos = 100 + (100 - self.players_positions[self.current_player])
                self.players_positions[self.current_player] = self.snakes_and_ladders.get(retreat_pos, retreat_pos)

            if self.players_positions[self.current_player] == 100:  # we got a winner!
                self.game_over = True
                return 'Player {} Wins!'.format(self.current_player + 1)

            game_progress_message = 'Player {} is on square {}'.format(self.current_player + 1,
                                                                       self.players_positions[self.current_player])
            if die1 != die2:  # both die values are the same - current player will have extra turn, otherwise - switch
                self.current_player = 1 % (2 - self.current_player)  # turns switch: transforms 1 to 0 and 0 to 1
            return game_progress_message
        return 'Game over!'
