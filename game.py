from console_manager import ConsoleManager

class Game():
    def __init__(self):
        self._players = []
        self._user_player = None

    def add_player(self, player):
        self._players.append(player)
        if player.is_user():
            self._user_player = player

    def user_player(self):
        return self._user_player

    def all_players(self):
        return self._players

    def is_over(self):
        return self.player_lost() or self.player_won()

    def player_lost(self):
        return self._user_player.is_dead()

    def player_won(self):
        return len(self.remaining_npcs()) == 0

    def remaining_npcs(self):
        return [p for p in self.all_players() if not p.is_user() and not p.is_dead()]

    def play(self):
        ConsoleManager.start_game()

        for index, turn in enumerate(self._create_turns()):
            ConsoleManager.start_round(index)

            turn.play(self)

            for player in self.all_players():
                ConsoleManager.print_stats(player)

        if self.player_won():
            ConsoleManager.player_won() 
        if self.player_lost():
            ConsoleManager.player_lost() 

    def _create_turns(self):
        return TurnIterator(self)

class Turn:
    def __init__(self, player):
        self._player = player

    def play(self, game):
        self._player.take_turn(game)

class TurnIterator:
    def __init__(self, game):
        self._game = game
        self._players = game.all_players()
        self._current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._game.is_over():
            raise StopIteration

        if self._current < len(self._players) - 1:
            self._current += 1
        else:
            self._current = 0

        current_player = self._players[self._current]
        return Turn(current_player)


