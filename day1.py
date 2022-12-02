f = open('Day 1\\inputday1.txt', 'r')
lines = f.readlines()

max_cal = 0
new_cal = 0
old_cal = 0
current_cal = 0
cal2 = 0
cal3 = 0
total_cal = 0
cal_list = []

for line in lines:
    old_line = line
    new_line = f.readline().strip()
    if line.strip() == "":
        cal_list.append(current_cal)
        current_cal = 0
        new_cal = 0
        old_cal = 0
    else:
        combined_cal = old_line + new_line
        new_cal = int(combined_cal)
        current_cal = new_cal + old_cal
        print(current_cal)
        if current_cal > max_cal:
            max_cal = current_cal
        old_cal = current_cal
    line = new_line
cal_list.sort()
max_cal = cal_list[-1]
cal2 = cal_list[-2]
cal3 = cal_list[-3]
total_cal = max_cal + cal2 + cal3
print(max_cal)
print(total_cal)