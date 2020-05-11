import Baseball.atbat as ab
import time


class Inning:
    def __init__(self, frame, num, score, battingpos):
        self.frame = frame
        self.num = num
        self.numouts = 0
        self.bases = Bases()
        self.score = score
        self.runs = 0
        self.battingpos = battingpos

    # pass in an inning parameter
    def addout(self):
        self.numouts += 1

    def showbases(self):
        if self.bases.firstoccupied() and self.bases.secondoccupied() and self.bases.thirdoccupied():
            print("Bases loaded")
        elif self.bases.secondoccupied() and self.bases.thirdoccupied():
            print("Runners on second and third")
        elif self.bases.thirdoccupied() and self.bases.firstoccupied():
            print("Runners on the corners")
        elif self.bases.firstoccupied() and self.bases.secondoccupied():
            print("Runners on first and second")
        elif self.bases.thirdoccupied():
            print("Man on third")
        elif self.bases.secondoccupied():
            print("Man on second")
        elif self.bases.firstoccupied():
            print("Man on first")


    def updatebases(self, baserunner, numbases):
        runstoadd = 0
        if numbases == 1:
            # update other bases and then add new runner
            # TODO: Add so that runners move varying amounts of bases

            # ORDER MATTERS HERE, MUST MOVE RUNNER THEN None the base
            if self.bases.thirdoccupied():
                print(self.bases.third, "scores")
                self.bases.third = None
                runstoadd += 1
            if self.bases.secondoccupied():
                self.bases.third = self.bases.second
                self.bases.second = None
            if self.bases.firstoccupied():
                self.bases.second = self.bases.first
                self.bases.first = None

            self.bases.first = baserunner

        elif numbases == 2:
            if self.bases.thirdoccupied():
                print(self.bases.third, "scores")
                self.bases.third = None
                runstoadd += 1
            if self.bases.secondoccupied():
                print(self.bases.second, "scores")
                self.bases.second = None
                runstoadd += 1
            if self.bases.firstoccupied():
                self.bases.second = self.bases.first
                self.bases.first = None

            self.bases.second = baserunner

        elif numbases == 3:
            if self.bases.thirdoccupied():
                print(self.bases.third, "scores")
                self.bases.third = None
                runstoadd += 1
            if self.bases.secondoccupied():
                print(self.bases.second, "scores")
                self.bases.second = None
                runstoadd += 1
            if self.bases.firstoccupied():
                print(self.bases.first, "scores")
                self.bases.first = None
                runstoadd += 1

            self.bases.third = baserunner

        else:

            if self.bases.thirdoccupied():
                print(self.bases.third, "scores")
                self.bases.third = None
                runstoadd += 1
            if self.bases.secondoccupied():
                print(self.bases.second, "scores")
                self.bases.second = None
                runstoadd += 1
            if self.bases.firstoccupied():
                print(self.bases.first, "scores")
                self.bases.first = None
                runstoadd += 1
            print(baserunner, "scores")
            runstoadd += 1

            if self.frame == "Top":
                self.score.awayscore += runstoadd
            else:
                self.score.homescore += runstoadd

            if runstoadd > 0:
                self.score.showscore()

            self.runs += runstoadd

    def showinning(self):
        print(self.frame, end='')
        if self.num == 1:
            print(" 1st")
        elif self.num == 2:
            print(" 2nd")
        elif self.num == 3:
            print(" 3rd")
        else:
            print(" " + str(self.num) + "th")



    def playinning(self, hometeam, awayteam, score):
        self.score = score

        self.showinning()
        self.score.showscore()

        i = self.battingpos
        while self.numouts < 3:
            # Reset lineup
            if i > 9:
                i = 1

            # Get ith batter out of lineup
            self.showinning()
            print(self.numouts, "outs")
            self.showbases()
            result = ab.atbat("Batter " + str(i), "Pitcher")

            if result == 0:
                self.addout()
            else:
                self.updatebases("Batter" + str(i), result)

            time.sleep(1)

            i += 1

        print("End of inning")


class Bases:
    def __init__(self):
        self.first = None
        self.second = None
        self.third = None

    def firstoccupied(self):
        return not self.first is None

    def secondoccupied(self):
        return not self.second is None

    def thirdoccupied(self):
        return not self.third is None

