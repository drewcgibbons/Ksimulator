import Baseball.data as bd


# tag is a 3 letter tag
class Team:
    def __init__(self, tag):
        self.tag = tag
        self.batters = bd.getbatters(tag)
        self.pitchers = bd.getpitchers(tag)
