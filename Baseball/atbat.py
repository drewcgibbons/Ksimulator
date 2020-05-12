import time
import Baseball.pitch as bp
import Baseball.batting as bb


class Count:
    def __init__(self):
        self.ball = 0
        self.strike = 0

    def addfoul(self):
        if self.strike != 2:
            self.strike += 1

    def addstrike(self):
        self.strike += 1

    def addball(self):
        self.ball += 1

    def showcount(self):
        print(self.ball, "-", self.strike)

# 1 is out
def atbat(battername, pitchername):
    # Create new count for each a/b
    pitcher = bp.Pitcher(pitchername)
    batter = bb.Batter(battername)
    count = Count()

    print("At Bat: ", batter.name)

    while count.ball < 4 and count.strike < 3:
        count.showcount()
        time.sleep(0.25)

        # Pitch and show results
        pitch = pitcher.pitch(count)
        pitcher.showpitch(pitch)
        batteraction = batter.action(pitch)

        time.sleep(0.25)
        if batteraction == 0:
            pitchval = processpitch(pitch)

            if pitchval == 1:
                count.addstrike()
            elif pitchval == 0:
                count.addball()

        elif batteraction == -1:
            print(batter.name, "fouls the pitch away\n")
            count.addfoul()

        elif batteraction > 0 and batteraction != 4 and batteraction != 5:
            print("Hit!\n")
            if batteraction == 1:
                print(batter.name, "gets on with a single\n")
                return 1
            elif batteraction == 2:
                print(batter.name, "gets on with a double\n")
                return 2
            elif batteraction == 3:
                print(batter.name, "gets on with a triple\n")
                return 3

        elif batteraction == 4:
            print("HOMERUN!\n")
            return 4

        elif batteraction < -1:
            # -2 fly out
            # -3 ground out
            # -4 lineout
            if batteraction == -2:
                print(batter.name, "flies out\n")
            elif batteraction == -3:
                print(batter.name, "grounds out\n")
            else:
                print(batter.name, "lines out\n")
            return 0

        elif batteraction == 5:
            print("Strike Swinging\n")
            count.addstrike()

        if batteraction <= -2:
            break

    #FIXME: WALK ACTS LIKE SINGLE, NEEDS SPECIAL CHECKING
    if count.ball == 4:
        print("Walk\n")
        return 6

    if count.strike == 3:
        print("Strikeout\n")
        return 0


# 1 is strike 0 is ball
def processpitch(pitch):
    if pitch.isstrike:
        print("Strike\n")
        return 1
    else:
        print("Ball\n")
        return 0
