# Gets the batters for a team
def getbatters(teamname):
    batters = dict()

    with open("players/batter.txt", "r", encoding= 'utf-8') as file:

        # Get to proper position
        while file.readline() != teamname:
            continue



    return batters