f = open('Day 2\\inputday2.txt', 'r')
lines = f.readlines()

MATCH_POINTS = {'A X':4, 'B Y':5, 'C Z':7, 'A Y':4, 'A Z':3, 'B X':1, 'B Z':9, 'C X':7, 'C Y':2}
#x = lose, y = tie, z = win
#a = rock, b = paper, c = scissors
#rock = 1, paper = 2, scissors = 3
match_points = 0
final_points = 0

for line in lines:
    #new_line = f.readline().strip()
    match_points = MATCH_POINTS[line.strip()]
    final_points += match_points
print(final_points)
