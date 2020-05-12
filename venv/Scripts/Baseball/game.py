import Baseball.inning as bi
import Baseball.score as bs
import Baseball.team as bt


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
        score = bs.Score(self.hometeam.name, self.awayteam.name)

        # Game is inning list, odd indicies are top, even are bottom
        game = list()
        i = 1
        while i <= 9:
            game.append(bi.Inning("Top", i, score, self.awayteam, self.awaybattingpos))
            game.append(bi.Inning("Bottom", i, score, self.hometeam, self.homebattingpos))

            self.awaybattingpos = game[2 * i - 2].playinning(self.hometeam, self.awayteam, score)

            if i != 9 or self.hometeamruns <= self.awayteamruns:
                self.homebattingpos = game[2 * i - 1].playinning(self.hometeam, self.awayteam, score)

            i += 1

        # Extra innings
        if i > 9 and score.awayscore == score.homescore:
            while score.awayscore == score.homescore:
                game.append(bi.Inning("Top", i, score, self.awayteam, self.awaybattingpos))
                game.append(bi.Inning("Bottom", i, score, self.hometeam, self.homebattingpos))

                self.awaybattingpos = game[2 * i - 2].playinning(self.hometeam, self.awayteam, score)
                self.homebattingpos = game[2 * i - 1].playinning(self.hometeam, self.awayteam, score)

                i += 1
        score.showscore()
        print("Final")

        return self.hometeamruns > self.awayteamruns

class Series:
    def __init__(self, firstteam, secondteam):
        self.firstteam = firstteam
        self.secondteam = secondteam

    def playseries(self):
        firstteamwins = 0
        secondteamwins = 0

        i = 0
        # First two games first team is at home
        while i <= 2:
            i += 1
            print("Game:", i)
            game = Game(self.firstteam, self.secondteam)
            result = game.runGame()
            if result == True:
                firstteamwins += 1
            else:
                secondteamwins += 1

            if firstteamwins > secondteamwins:
                print(self.firstteam.name, "leads series", firstteamwins, "-", secondteamwins)
            elif secondteamwins > firstteamwins:
                print(self.secondteam.name, "leads series", secondteamwins, "-", firstteamwins)
            else:
                print("Series tied", firstteamwins, "-", secondteamwins)

        while i <= 5:
            i += 1
            print("Game:", i)
            game = Game(self.secondteam, self.firstteam)
            result = game.runGame()
            if result == True:
                firstteamwins += 1
            else:
                secondteamwins += 1

            if secondteamwins >= 4 or firstteamwins >= 4:
                break

            if firstteamwins > secondteamwins:
                print(self.firstteam.name, "leads series", firstteamwins, "-", secondteamwins)
            elif secondteamwins > firstteamwins:
                print(self.secondteam.name, "leads series", secondteamwins, "-", firstteamwins)
            else:
                print("Series tied", firstteamwins, "-", secondteamwins)

        while i <= 7 and secondteamwins < 4 and firstteamwins < 4:
            i += 1
            print("Game:", i)
            game = Game(self.firstteam, self.secondteam)
            result = game.runGame()

            if result == True:
                firstteamwins += 1
            else:
                secondteamwins += 1

                if secondteamwins >= 4 or firstteamwins >= 4:
                    break

            if firstteamwins > secondteamwins:
                print(self.firstteam.name, "leads series", firstteamwins, "-", secondteamwins)
            elif secondteamwins > firstteamwins:
                print(self.secondteam.name, "leads series", secondteamwins, "-", firstteamwins)
            else:
                print("Series tied", firstteamwins, "-", secondteamwins)

        if firstteamwins > secondteamwins:
            print(self.firstteam.name, "win series", firstteamwins, "-", secondteamwins)
        else:
            print(self.secondteam.name, "win series", secondteamwins, "-", firstteamwins)
