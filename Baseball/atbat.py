import time
import Baseball.pitch as bp


class Count:
    def __init__(self):
        self.ball = 0
        self.strike = 0

    def foul(self):
        if self.strike != 2:
            self.strike += 1

    def addstrike(self):
        self.strike += 1

    def addball(self):
        self.ball += 1

    def showcount(self):
        print(self.ball, "-", self.strike)


def atbat(battername, pitchername):
    # Create new count for each a/b
    pitcher = bp.Pitcher(pitchername)
    count = Count()

    print("At Bat: ", battername)

    while count.ball < 4 and count.strike < 3:
        count.showcount()
        time.sleep(1)

        pitch = pitcher.pitch(count)
        pitchval = processpitch(pitch)
        time.sleep(2)
        # show pitch
        pitcher.showpitch(pitch)
        if pitchval == 1:
            count.addstrike()
        elif pitchval == 0:
            count.addball()

    if count.ball == 4:
        print("Walk")

    if count.strike == 3:
        print ("Strikeout")


# 1 is strike 0 is ball
def processpitch(pitch):
    xcount = 4
    ycount = 4
    STRIKEXMIN = 1
    STRIKEXMAX = 3
    STRIKEYMIN = 1
    STRIKEYMAX = 3

    if STRIKEXMIN <= pitch.location.x <= STRIKEXMAX and STRIKEYMIN <= pitch.location.y <= STRIKEYMAX:
        print("Strike")
        return 1
    else:
        print("Ball")
        return 0
