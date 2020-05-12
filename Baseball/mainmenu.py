import Baseball.atbat
import Baseball.game as bg

def mainmenu():
    while True:
        print("Use the keyboard to select the following (and press enter)")
        print("1.) Play")
        print("2.) Watch Simulation")
        print("3.) Exit")
        key = input()
        if key == '1':
            pass
        if key == '2':
            #teams = teamselect()
            game = bg.Game("Astros", "Dodgers")
            game.runGame()
        if key == '3':
            break

def teamselect():
    teams = list()
    # Pick Team
    while True:
        print("Pick the first team from the following menus")
        print("1.)")
        key = input()


    while True:
        print ("Pick the second team")

    return teams