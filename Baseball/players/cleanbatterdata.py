import fileinput
import re

with open("lineups.txt", 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:

        new_line = re.match("\w+,\w+.\w+\\w+.\w+", line, re.U)

        print(new_line)


