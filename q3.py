import sys


def least_cnt(start_in, end_in, flag1, flag2):
    cnt_in = 0
    if flag1 == flag2:
        return end_in - start_in + 1

    elif flag1 or flag2:

        if end_in - start_in + 1 == 1:
            cnt_in += 2

        elif end_in - start_in + 1 == 2:
            cnt_in += 4

        elif end_in - start_in + 1 > 2:
            cnt_in += 2 * (end_in - start_in + 1)

    return cnt_in


a = input()
for line in sys.stdin:
    line = line.strip()
    if len(line) == 0:
        print(0)
    cnt = 0
    up_low_flag = False  # False 表示小写
    start = 0
    end = 0
    alpha_flag = line[0].isupper()  # False 表示小写
    for j in range(1, len(line)):
        if alpha_flag == line[j].isupper():
            end += 1
        else:
            if up_low_flag != alpha_flag and end - start + 1 > 1:
                up_low_flag = not up_low_flag
                cnt += 1
            cnt += least_cnt(start, end, up_low_flag, alpha_flag)
            print(cnt)
            start = j
            end = j
            alpha_flag = line[j].isupper()
    # if end - start + 1 == 1 and up_low_flag != alpha_flag:
    #     cnt += least_cnt(start, end, up_low_flag, alpha_flag)
    # else:
    if up_low_flag != alpha_flag and end - start + 1 > 1:
        up_low_flag = not up_low_flag
        cnt += 1
    cnt += least_cnt(start, end, up_low_flag, alpha_flag)
    print(cnt)

