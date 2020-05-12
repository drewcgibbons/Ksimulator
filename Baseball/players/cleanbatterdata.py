import fileinput
import re

with fileinput.FileInput("lineups.txt", inplace=True) as file:
    for line in file:
        new_line = re.match(",\w+.\w+\\w+,", line)
        print(new_line)


