import Baseball.game as bg
import Baseball.data as data
import Baseball.team as team


def mainmenu():
    while True:
        print("Use the keyboard to select the following (and press enter)")
        print("1.) Play")
        print("2.) Watch Simulation")
        print("3.) Exit")
        key = input()

        teamtags = data.TeamDict().teamdict

        if key == '1':
            pass
        if key == '2':
            # Corresponds w teamdict
            tags = teamselect()
            # Cancelled menu input
            if tags is None or len(tags) != 2:
                continue

            # Intialize with corresponding teamtags in Data
            hometeam = team.Team(teamtags[tags[0]][0], teamtags[tags[0]][1])
            awayteam = team.Team(teamtags[tags[1]][0], teamtags[tags[1]][1])

            game = bg.Game(hometeam, awayteam)
            game.runGame()
        if key == '3':
            break

def teamselect():
    teams = list()
    # Key 1,2 combo will map to a team
    key1 = teamint1 = key2 = teamint2 = -1

    validinput = False

    # Pick Team
    while not validinput:
        print("Pick the first team from the following divisions")
        showdivmenu()
        key1 = input()

        if 1 <= int(key1) <= 6:
            validinput = True
            teamint1 = showdivteams(int(key1))
            if teamint1 == 6:
                continue

        elif int(key1) == 7:
            return None

    validinput = False

    # Pick 2nd team
    while not validinput:
        print("Pick the second team from the following divisions")
        showdivmenu()
        key2 = input()

        if 1 <= int(key2) <= 6:
            validinput = True
            teamint2 = showdivteams(int(key2))
            if teamint2 == 6:
                continue

        elif int(key2) == 7:
            return None

    teams.append(teamint1)
    teams.append(teamint2)

    return teams


def showdivmenu():
    print("1.) NL East")
    print("2.) NL Central")
    print("3.) NL West")
    print("4.) AL East")
    print("5.) AL Central")
    print("6.) AL West")
    print("7.) Go Back")


def showdivteams(divnum):
    key = -1

    while key < 1 or key > 6:
        print("Select a team")

        if divnum == 1:
            print("1.) Atlanta Braves")
            print("2.) Miami Marlins")
            print("3.) New York Mets")
            print("4.) Philadelphia Phillies")
            print("5.) Washington Nationals")
        elif divnum == 2:
            print("1.) Chicago Cubs")
            print("2.) Cincinnati Reds")
            print("3.) Milwaukee Brewers")
            print("4.) Pittsburgh Pirates")
            print("5.) St. Louis Cardinals")
        elif divnum == 3:
            print("1.) Arizona Diamondbacks")
            print("2.) Colorado Rockies")
            print("3.) LA Dodgers")
            print("4.) San Diego Padres")
            print("5.) San Francisco Giants")
        elif divnum == 4:
            print("1.) Baltimore Orioles")
            print("2.) Boston Red Sox")
            print("3.) New York Yankees")
            print("4.) Tampa Bay Rays")
            print("5.) Toronto Blue Jays")
        elif divnum == 5:
            print("1.) Cleveland Indians")
            print("2.) Chicago White Sox")
            print("3.) Detroit Tigers")
            print("4.) Kansas City Royals")
            print("5.) Minnesota Twins")
        elif divnum == 6:
            print("1.) Houston Astros")
            print("2.) LA Angels")
            print("3.) Oakland Athletics")
            print("4.) Seattle Mariners")
            print("5.) Texas Rangers")
        print("6.) Go Back")

        key = input()
        key = int(key)

    # Do calculation to get proper teamnum for teamdict
    teamnum = (divnum - 1) * 5 + key

    return teamnum

