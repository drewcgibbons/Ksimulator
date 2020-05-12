import fileinput
import re

with open("lineups.txt", 'r', encoding='utf-8') as file:
    lines = file.readlines()
    writefile = open("batters.txt", 'w+', encoding='utf-8')

    for line in lines:
        teamname = re.match("[A-Z]{2,3}", line, re.U)

        # gets format group 1 is (1,position,firstname optionalmiddlenames lastname suffix)
        nl = re.match("(\d+,\w+,[\w\.]+[\s\w]+\.?)[*#]?\\\\\w+(.+)", line, re.U)
        if nl is not None:
            writefile.write("\n" + nl.group(1) + nl.group(2))
        if teamname is not None:
            writefile.write("\n" + str(teamname.group(0)))

