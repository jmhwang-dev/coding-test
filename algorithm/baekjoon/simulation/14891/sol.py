# 14891
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

GEARS = [input().strip() for _ in range(4)]
K = int(input())

SEQUENCE = [list(map(int, input().split())) for _ in range(K)]
# print(SEQUENCE)
# print(GEARS, K)


# 톱니바퀴 A를 회전할 때, 그 옆에 있는 톱니바퀴 B와
# 서로 맞닿은 톱니의 극이 다르다면, B는 A가 회전한 방향과 반대방향으로 회전하게 된다. 
# 같으면 회전 안함

def roate_ccw(target_gear):
    tmp_gear = target_gear[1:]
    tmp_gear += target_gear[0]
    return tmp_gear

def rotate_cw(target_gear):
    tmp_gear = target_gear[-1]
    tmp_gear += target_gear[0:-1]
    return tmp_gear

def roate_gear(gear_index, direction):
    global GEARS

    init_gears = [ gear[:] for gear in GEARS]

    # 2, 6번이 연결되는 톱니
    # left
    curr_gear_index = gear_index
    left_index = curr_gear_index - 1
    curr_direction = direction
    connected_gear = [[gear_index, direction]]

    while left_index >= 0:
        if init_gears[left_index][2] != init_gears[curr_gear_index][6]:
            connected_gear.append([left_index, curr_direction * -1])
            curr_direction = curr_direction * -1
        else:
            break

        curr_gear_index = left_index
        left_index = curr_gear_index - 1

    # right
    curr_gear_index = gear_index
    right_index = curr_gear_index + 1
    curr_direction = direction
    while right_index < 4:
        if init_gears[right_index][6] != init_gears[curr_gear_index][2]:
            connected_gear.append([right_index, curr_direction * -1])
            curr_direction = curr_direction * -1
        else:
            break

        curr_gear_index = right_index
        right_index = curr_gear_index + 1
    
    # print(connected_gear)
    for gear_index, direction in connected_gear:
    
        if direction == -1:
            new_gear = roate_ccw(init_gears[gear_index])
        else:
            new_gear = rotate_cw(init_gears[gear_index])

        GEARS[gear_index] = new_gear
    
    # print(GEARS)

def get_score():
    # 12시 방향은 0번 인덱스
    # N극은 0, S극은 1로 나타나있다.
    total_score = 0
    for i in range(4):
        if i == 0:
            score = 1
        
        elif i == 1:
            score = 2

        elif i == 2:
            score = 4
        
        elif i == 3:
            score = 8

        if GEARS[i][0] == '1':
            total_score += score

    return total_score

for gear, direction in SEQUENCE:
    roate_gear(gear-1, direction)

total_score = get_score()
print(total_score)