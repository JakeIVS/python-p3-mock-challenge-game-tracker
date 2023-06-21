class Game:
    def __init__(self, title):
        self.title = title
        self._results = []
        self._players = []
        
    @property
    def title(self):
        return self._title 
    @title.setter
    def title(self, title):
        if type(title) == str and len(title) > 0 and not hasattr(self, 'title'):
            self._title = title
        else:
            raise Exception('Title must be a string, and must not already exist')
        

    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results
    
    def players(self, new_player=None):
        from classes.player import Player
        if new_player and isinstance(new_player, Player) and new_player not in self._players:
            self._players.append(new_player)
        return self._players
    
    def average_score(self, player):
        total_score = 0
        for result in player._results:
            total_score += result.score
        return total_score / len(player._results)