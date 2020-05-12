class Score:
    def __init__(self, hometeam, awayteam):
        self.homescore = 0
        self.awayscore = 0
        self.hometeam = hometeam
        self.awayteam = awayteam

    def showscore(self):
        print(self.awayteam, ":", self.awayscore)
        print(self.hometeam, ":", self.homescore)

    def showformatscore(self, numinnings, inninglist):
        i = 1
        while i <= numinnings:
            print(i, end='')
            # top of innings is 2x-2 index,
            print(inninglist[2*i - 2], end='')
            print(inninglist[2*i - 1], end='')


