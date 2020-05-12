import re
import Baseball.player as bp
import os

# Gets the batters for a team from file
def getbatters(teamname):
    batters = dict()
    print(teamname)
    print(os.getcwd())
    with open("players/batters.txt", "r", encoding='utf-8') as file:

        # Get to proper position
        while file.readline() != teamname:
            continue

        # read and process data
        while True:
            line = file.readline()

            # Read til next team name
            teamname = re.match("[A-Z]{3}", line)
            if teamname:
                break

            # tokenize line
            tokens = line.split(",")

            # create player and add to dict
            nameparts = tokens[2].split(" ")

            # separate name parts
            if len(nameparts) == 2:
                fname = nameparts[0]
                lname = nameparts[1]

            # Edge case for 3 length names e.g (John Paul Jones or Ken Griffey Jr.)
            elif len(nameparts) == 3:
                if nameparts[2] == "Jr.":
                    fname = nameparts[0]
                    lname = nameparts[1] + nameparts[2]
                else:
                    fname = nameparts[0] + nameparts[1]
                    lname = nameparts[2]

            # Create player and add to list
            tempplayer = bp.Player(fname, lname, tokens[1])
            batters[int(tokens[0])] = tempplayer

    return batters


class TeamDict:
    def __init__(self):
        self._teamdict = dict()

        # NL East
        self._teamdict[1] = ["ATL", "Braves"]
        self._teamdict[2] = ["MIA", "Marlins"]
        self._teamdict[3] = ["NYM", "Mets"]
        self._teamdict[4] = ["PHI", "Phillies"]
        self._teamdict[5] = ["WSN", "Nationals"]

        # NL Central
        self._teamdict[6] = ["CHC", "Cubs"]
        self._teamdict[7] = ["CIN", "Reds"]
        self._teamdict[8] = ["MIL", "Brewers"]
        self._teamdict[9] = ["PIT", "Pirates"]
        self._teamdict[10] = ["STL", "Cardinals"]

        # NL West
        self._teamdict[11] = ["ARI", "Diamondbacks"]
        self._teamdict[12] = ["COL", "Rockies"]
        self._teamdict[13] = ["LAD", "Dodgers"]
        self._teamdict[14] = ["SDP", "Padres"]
        self._teamdict[15] = ["SFG", "Giants"]

        # AL East
        self._teamdict[16] = ["BAL", "Orioles"]
        self._teamdict[17] = ["BOS", "Red Sox"]
        self._teamdict[18] = ["NYY", "Yankees"]
        self._teamdict[19] = ["TBR", "Rays"]
        self._teamdict[20] = ["TOR", "Blue Jays"]

        # AL Central
        self._teamdict[21] = ["CLE", "Indians"]
        self._teamdict[22] = ["CWS", "White Sox"]
        self._teamdict[23] = ["DET", "Tigers"]
        self._teamdict[24] = ["KCR", "Royals"]
        self._teamdict[25] = ["MIN", "Twins"]

        # AL West
        self._teamdict[26] = ["HOU", "Astros"]
        self._teamdict[27] = ["LAA", "Angels"]
        self._teamdict[28] = ["OAK", "Athletics"]
        self._teamdict[29] = ["SEA", "Mariners"]
        self._teamdict[30] = ["TEX", "Rangers"]

    @property
    def teamdict(self):
        return self._teamdict