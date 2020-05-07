while ()




class Count:
    def __init__(self):
        self.ball = 0
        self.strike = 0

    def foul(self):
        if self.strike != 2:
            self.strike += 1

    def strike(self):
        self.strike += 1

    def ball(self):
        self.ball += 1