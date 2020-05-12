import re
import Baseball.batting as batter
import pathlib

# Gets the batters for a team from file
def getbatters(teamname):
    batters = dict()
    with open("Baseball/players/batters.txt", "r", encoding='utf-8') as file:

        teamtag = ""
        # Get to proper position
        while teamtag != teamname:
            line = file.readline()

            # Read til next team name
            teamtag = re.match("[A-Z]{3}", line)
            if teamtag is not None:
                teamtag = teamtag.group(0)


        # read and process data
        while True:
            line = file.readline()

            # Read til next team name
            teamtag = re.match("[A-Z]{3}", line)
            if teamtag:
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
                    lname = nameparts[1] + " " + nameparts[2]
                else:
                    fname = nameparts[0] + " " + nameparts[1]
                    lname = nameparts[2]

            # Create player and add to list
            tempplayer = batter.Batter(fname, lname, tokens[1])
            batters[int(tokens[0])] = tempplayer

    return batters


class TeamDict:
    def __init__(self):
        self._teamdict = dict()

        # AL East
        self._teamdict[1] = ["BAL", "Orioles"]
        self._teamdict[2] = ["BOS", "Red Sox"]
        self._teamdict[3] = ["NYY", "Yankees"]
        self._teamdict[4] = ["TBR", "Rays"]
        self._teamdict[5] = ["TOR", "Blue Jays"]

        # AL Central
        self._teamdict[6] = ["CLE", "Indians"]
        self._teamdict[7] = ["CWS", "White Sox"]
        self._teamdict[8] = ["DET", "Tigers"]
        self._teamdict[9] = ["KCR", "Royals"]
        self._teamdict[10] = ["MIN", "Twins"]

        # AL West
        self._teamdict[11] = ["HOU", "Astros"]
        self._teamdict[12] = ["LAA", "Angels"]
        self._teamdict[13] = ["OAK", "Athletics"]
        self._teamdict[14] = ["SEA", "Mariners"]
        self._teamdict[15] = ["TEX", "Rangers"]

        # NL East
        self._teamdict[16] = ["ATL", "Braves"]
        self._teamdict[17] = ["MIA", "Marlins"]
        self._teamdict[18] = ["NYM", "Mets"]
        self._teamdict[19] = ["PHI", "Phillies"]
        self._teamdict[20] = ["WSN", "Nationals"]

        # NL Central
        self._teamdict[21] = ["CHC", "Cubs"]
        self._teamdict[22] = ["CIN", "Reds"]
        self._teamdict[23] = ["MIL", "Brewers"]
        self._teamdict[24] = ["PIT", "Pirates"]
        self._teamdict[25] = ["STL", "Cardinals"]

        # NL West
        self._teamdict[26] = ["ARI", "Diamondbacks"]
        self._teamdict[27] = ["COL", "Rockies"]
        self._teamdict[28] = ["LAD", "Dodgers"]
        self._teamdict[29] = ["SDP", "Padres"]
        self._teamdict[30] = ["SFG", "Giants"]


    @property
    def teamdict(self):
        return self._teamdict