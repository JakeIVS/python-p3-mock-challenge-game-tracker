class Result:

    all = []

    def __init__(self, player, game, score):
        self._player = player
        self._game = game
        self.score = score

        Result.all.append(self)
        
        player.results(self)
        player.games_played(game)

        game.results(self)
        game.players(player)

    @property
    def score(self):
        return self._score 
    @score.setter
    def score(self, score):
        if type(score) == int and 1<= score <= 5000:
            self._score = score
        else:
            raise Exception('Score must be an integer from 1-5000.')
    
    @property
    def player(self):
        return self._player
    @player.setter
    def player(self, player):
        from lib.classes.player import Player
        if isinstance(player, Player):
            self._player = player
    
    @property
    def game(self):
        return self._game
    @game.setter
    def game(self, game):
        from lib.classes.game import Game
        if isinstance(game,Game):
            self._game = game
