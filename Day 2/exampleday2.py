f = open('Day 1\\example2.txt', 'r')
lines = f.readlines()

POINTS = {'X':1, 'Y':2, 'Z':3}

max_cal = 0
new_cal = 0
old_cal = 0
current_cal = 0

for line in lines:
    old_line = line
    new_line = f.readline().strip()