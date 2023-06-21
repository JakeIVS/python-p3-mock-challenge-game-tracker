class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []
        self._count_games = {}
        Player.all.append(self)
        
    @property
    def username(self):
        return self._username 
    @username.setter
    def username(self, username):
        if type(username) == str and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception('Username must be between 2 and 16 characters long.')

    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results
    
    def games_played(self, new_game=None):
        from classes.game import Game
        if new_game and isinstance(new_game, Game) and new_game not in self._games_played:
            self._games_played.append(new_game)
            self._count_games[new_game] = 1
        elif new_game and isinstance(new_game, Game):
            self._count_games[new_game] += 1
        return self._games_played
    
    def played_game(self, game):
        return game in self._games_played
    
    def num_times_played(self, game):
        if game in self._count_games:
            return self._count_games[game]
        else:
            return 0
    
    @classmethod
    def highest_scored(cls, game):
        from lib.classes.game import Game
        player_averages = {}
        if isinstance(game, Game) and not game._players == []:
            for player in game._players:
                player_averages[player] = game.average_score(player)
        return max(player_averages, key=player_averages.get)

