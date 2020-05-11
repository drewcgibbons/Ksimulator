import Baseball.inning as bi


class Game:
    def __init__(self, hometeam, awayteam):
        self.hometeam = hometeam
        self.awayteam = awayteam
        self.hometeamruns = 0
        self.awayteamruns = 0

    def runGame(self):
        # Initialize inning array
        game = list()
        i = 1
        while i < 9:
            game.append(bi.Inning("Top", i))
            game.append(bi.Inning("Bottom", i))
