import sys

line = input()

line = line.strip().split()

lenght_list = [len(w) for w in line]

min_length = min(lenght_list)

common_str = ""
for i in range(min_length):
    a = line[0][i]
    flag = True
    for j in range(1, len(line)):
        if a != line[j][i]:
            flag = False
            break
    if not flag:
        break
    else:
        common_str += a
print(common_str)
