import Baseball.data as bd


class Team:
    # tag is a 3 letter tag
    def __init__(self, tag, name):
        self.tag = tag
        self.name = name
        self.batters = bd.getbatters(tag)
        self.battingorder = dict()
        self._setbattingorder()
        # TODO: IMPLEMENT PITCHERS IN DATA
        # self.pitchers = bd.getpitchers(tag)

    def _setbattingorder(self):
        self.battingorder[0] = None

        i = 1

        # TODO: Set and Have a proper batting order lookup from a file
        while i <= 9:
            self.battingorder[i] = self.batters[i]
            i += 1
