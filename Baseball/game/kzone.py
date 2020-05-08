class Strikezone():
    xcount = 4
    ycount = 4
    STRIKEXMIN = 1
    STRIKEXMAX = 3
    STRIKEYMIN = 1
    STRIKEYMAX = 3

    def __init__(self):
        pass
    def process(self, x, y, count):
        if x <= self.STRIKEXMIN and x <= self.STRIKEXMAX and y <= self.STRIKEYMIN and y <= self.STRIKEYMAX:
            print("Strike")
        else:
            print("Ball")
