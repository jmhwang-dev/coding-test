def count_meeting(schedules=[[1, 4], [7, 8], [3, 5],[0, 6],[5, 7],[3, 8],[5, 9],[6, 10],[8, 11],[8, 12],[2, 13],[12, 14]]):
    order_by_start = sorted(schedules, key=lambda x: x[0])
    order_by_end = sorted(order_by_start, key=lambda x: x[1])
    # ordered = schedule.sort(key=lambda x: (x[1], x[0]))
    
    count = 0
    current_end_time = -1
    for schedule in order_by_end:
        if current_end_time > schedule[0]:
            continue
        current_end_time = schedule[1]
        count += 1
    return count
    
if __name__=="__main__":
    print(count_meeting(schedules=[[3,3], [1,3]]))
    exit()
    N = int(input())
    schedules = [list(map(int, input().split())) for _ in range(N)]
    print(count_meeting(schedules))