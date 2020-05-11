class Inning:
    def __init__(self, frame, num):
        self.frame = frame
        self.num = num
        self.numouts = 0

# pass in an inning parameter
def out(inning):
    inning.numouts += 1
