import fileinput
import re

with open("lineups.txt", 'r', encoding='utf-8') as file:
    lines = file.readlines()
    # writefile = open("batters.txt", 'w+', encoding='utf-8')

    for line in lines:
        teamname = re.match("[A-Z]{2,3}", line, re.U)
        nl = re.match("(\d+,\w+,[\w\.]+.\w+)[*#]?\\\\\w+(.+)", line, re.U)
        if nl is not None:
            print(nl.group(1) + nl.group(2))
        if teamname is not None:
            print("\n" + str(teamname.group(0)))

