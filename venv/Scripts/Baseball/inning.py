import Baseball.atbat as ab
import time
import random


class Inning:
    def __init__(self, frame, num, score, team, battingpos):
        self.frame = frame
        self.num = num
        self.team = team
        self.numouts = 0
        self.bases = Bases()
        self.score = score
        self.runs = 0
        self.battingpos = battingpos

    # RETURN VALUE IS POSITION IN BATTING ORDER
    def playinning(self, hometeam, awayteam, score):
        self.score = score
        self.showinning()
        self.score.showscore()

        i = self.battingpos
        while self.numouts < 3:
            # Reset lineup
            if i > 9:
                i = 1

            # Check for walkoff starting in bottom of 9th
            if self.checkwalkoff():
                return

            # Get ith batter out of lineup
            self.showinning()
            print(self.numouts, "outs")
            self.showbases()
            print()
            time.sleep(1)

            # Steal and recheck outs
            self.trysteal()
            if self.numouts >= 3:
                break

            # At bat
            result = ab.atbat(self.team.battingorder[i], "Pitcher")

            if result == 0:
                self.addout()
            else:
                self.updatebases(self.team.battingorder[i], result)

            i += 1

        print("End of inning")
        return i

    def checkwalkoff(self):
        if self.num >= 9 and self.frame == "Bottom" and self.score.homescore > self.score.awayscore:
            return True

    # pass in an inning parameter
    def addout(self):
        self.numouts += 1

    def trysteal(self):
        stealattempt = random.randint(1, 100)

        if self.bases.firstoccupied() and not self.bases.secondoccupied():
            if stealattempt > 65:
                print(self.bases.first.lastname, "is trying to steal second")
                time.sleep(.5)

                # Try to throw out runner
                throwattempt = random.randint(66, 78)

                # Caught stealing
                if throwattempt > stealattempt:
                    print("OUT!", self.bases.first.lastname, "is caught stealing")
                    self.bases.first = None
                    self.addout()
                else:
                    print(self.bases.first.lastname, "stole second")
                    self.bases.second = self.bases.first
                    self.bases.first = None
                    time.sleep(.5)

        elif self.bases.secondoccupied() and not self.bases.thirdoccupied():
            if stealattempt > 85:
                print(self.bases.second.lastname, "is trying to steal third")
                time.sleep(.5)

                # Try to throw out runner
                throwattempt = random.randint(86, 92)

                # Caught stealing
                if throwattempt > stealattempt:
                    print("OUT!", self.bases.second.lastname, "is caught stealing")
                    self.bases.second = None
                    self.addout()
                else:
                    print(self.bases.second.lastname, "stole third")
                    self.bases.third = self.bases.second
                    self.bases.second = None
                    time.sleep(.5)

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
        # Single
        if numbases == 1:
            # update other bases and then add new runner
            # TODO: Add so that runners move varying amounts of bases

            # ORDER MATTERS HERE, MUST MOVE RUNNER THEN None the base
            if self.bases.thirdoccupied():
                print(self.bases.third.lastname, "scores")
                self.bases.third = None
                runstoadd += 1
            if self.bases.secondoccupied():
                self.bases.third = self.bases.second
                self.bases.second = None
            if self.bases.firstoccupied():
                self.bases.second = self.bases.first
                self.bases.first = None

            self.bases.first = baserunner

        # Walk
        # Must check iteratively for walks
        elif numbases == 6:
            if self.bases.firstoccupied():
                if self.bases.secondoccupied():
                    if self.bases.thirdoccupied():
                        self.bases.third = None
                        runstoadd +=1
                        print(self.bases.third.lastname, "scores")
                    self.bases.third = self.bases.second
                    self.bases.second = None
                self.bases.second = self.bases.first
                self.bases.first = None
            self.bases.first = baserunner


        elif numbases == 2:
            if self.bases.thirdoccupied():
                print(self.bases.third.lastname, "scores")
                self.bases.third = None
                runstoadd += 1
            if self.bases.secondoccupied():
                print(self.bases.second.lastname, "scores")
                self.bases.second = None
                runstoadd += 1
            if self.bases.firstoccupied():
                self.bases.second = self.bases.first
                self.bases.first = None

            self.bases.second = baserunner

        elif numbases == 3:
            if self.bases.thirdoccupied():
                print(self.bases.third.lastname, "scores")
                self.bases.third = None
                runstoadd += 1
            if self.bases.secondoccupied():
                print(self.bases.second.lastname, "scores")
                self.bases.second = None
                runstoadd += 1
            if self.bases.firstoccupied():
                print(self.bases.first.lastname, "scores")
                self.bases.first = None
                runstoadd += 1

            self.bases.third = baserunner

        else:

            if self.bases.thirdoccupied():
                print(self.bases.third.lastname, "scores")
                self.bases.third = None
                runstoadd += 1
            if self.bases.secondoccupied():
                print(self.bases.second.lastname, "scores")
                self.bases.second = None
                runstoadd += 1
            if self.bases.firstoccupied():
                print(self.bases.first.lastname, "scores")
                self.bases.first = None
                runstoadd += 1
            print(baserunner.lastname, "scores")
            runstoadd += 1

        if runstoadd != 0:
            if self.frame == "Top":
                self.score.awayscore += runstoadd
            else:
                self.score.homescore += runstoadd

            self.score.showscore()
            time.sleep(1)

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

