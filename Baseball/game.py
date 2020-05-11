import Baseball.inning as bi
import Baseball.score as bs

class Game:
    def __init__(self, hometeam, awayteam):
        self.hometeam = hometeam
        self.awayteam = awayteam
        self.hometeamruns = 0
        self.awayteamruns = 0
        self.homebattingpos = 1
        self.awaybattingpos = 1

    def runGame(self):
        # Initialize inning array
        score = bs.Score(self.hometeam, self.awayteam)

        # Game is inning list, odd indicies are top, even are bottom
        game = list()
        i = 1
        while i < 9:


            game.append(bi.Inning("Top", i, score, self.awaybattingpos))
            game.append(bi.Inning("Bottom", i, score, self.homebattingpos))

            game[2 * i - 2].playinning(self.hometeam, self.awayteam, score)
            game[2 * i - 1].playinning(self.hometeam, self.awayteam, score)

            i += 1

        # Extra innings
        if i == 9 and score.awayscore == score.homescore:
            while score.awayscore == score.homescore:
                game.append(bi.Inning("Top", i, score))
                game.append(bi.Inning("Bottom", i, score))

                game[2 * i - 2].playinning(self.hometeam, self.awayteam, score)
                game[2 * i - 1].playinning(self.hometeam, self.awayteam, score)

                i += 1

        else:
            score.showformatscore(i, game)
