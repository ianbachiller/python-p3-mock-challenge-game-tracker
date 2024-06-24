class Game:
    def __init__(self, title):
        self._title = None
        self._results = []
        self._players = []
        self.title = title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str):
            raise TypeError('Title must be a string.')
        if len(new_title) == 0:
            raise ValueError('Title must have more than 0 characters.')
        if hasattr(self, '_title') and self._title is not None:
            raise AttributeError('Title cannot be changed once set.')
        self._title = new_title

    def results(self):
        return self._results

    def players(self):
        return list(set([result.player for result in self._results]))  

    def average_score(self, player):
        scores = [result.score for result in self._results if result.player == player]
        if not scores:
            return 0
        return sum(scores) / len(scores)


class Player:
    def __init__(self, username):
        self._username = None
        self._results = []
        self.username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if not isinstance(new_username, str):
            raise TypeError('Username must be a string.')
        if len(new_username) < 2 or len(new_username) > 16:
            raise ValueError('Username must be between 2 and 16 characters.')
        self._username = new_username

    def results(self):
        return self._results

    def games_played(self):
        return list(set([result.game for result in self._results]))  

    def played_game(self, game):
        return any(result.game == game for result in self._results)

    def num_times_played(self, game):
        return sum(1 for result in self._results if result.game == game)


class Result:
    all = [] 

    def __init__(self, player, game, score):
        self._player = None
        self._game = None
        self._score = None
        self.player = player
        self.game = game
        self.score = score
        self.game._results.append(self)
        self.player._results.append(self)
        Result.all.append(self) 

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, new_player):
        if not isinstance(new_player, Player):
            raise TypeError('Player must be an instance of Player class.')
        self._player = new_player

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, new_game):
        if not isinstance(new_game, Game):
            raise TypeError('Game must be an instance of Game class.')
        self._game = new_game

    @property
    def score(self):
        return self._score


    @score.setter
    def score(self, new_score):
        self._score = new_score



