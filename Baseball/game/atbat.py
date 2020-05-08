import time


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


def atbat(batter, pitcher):
    # Create new count for each a/b
    count = Count()
    while count.ball < 4 and count.strike < 3:
        pitcher.throwpitch()
        time.sleep(2)






