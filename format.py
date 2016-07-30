import os,re

def reformat(file):
    lines = []
    f = open('lists/' + file, 'r')
    for i, line in enumerate(f):
        newLine = re.sub('^\d*:?\s?', str(i + 1) + ': ', line)
        lines.append(newLine)
    f.close()
    f = open('lists/' + file, 'w')
    for line in lines:
        f.write(line)
    f.close()


for file in os.listdir("lists/"):
    reformat(file)
