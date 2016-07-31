import sys, glob, re

del sys.argv[0]
files = []
setting = "1-5"
for arg in sys.argv:
    if glob.glob(arg):
        for file in glob.glob(arg):
            files.append(file)
    else:
        setting = arg

for file in files:
    f = open(file, 'r')
    first = int(re.search('^(\d+)-', setting).group(1)) if re.search('^(\d+)-', setting) else 1
    last = int(re.search('^(\d*-)?(\d+)$', setting).group(2)) if re.search('(^\d*-)?(\d+)$', setting) else sys.maxint
    for i, line in enumerate(f):
        if i + 1 >= first and i + 1 <= last:
            print line[:-1]
    f.close()
