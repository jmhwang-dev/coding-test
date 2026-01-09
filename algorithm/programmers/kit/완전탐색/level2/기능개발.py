from collections import deque

def solution(progresses, speeds):
    answer = []
    
    deploy = deque()
    for i in range(len(speeds)):
        day = 1
        cur_progress = progresses[i]
        while True:
            if cur_progress + speeds[i] * day < 100:
                day += 1
                continue
            deploy.append(day)
            break
    
    print(deploy)
    curr_d = deploy.popleft()
    cnt = 1
    
    while deploy:
        next_d = deploy[0]
        
        if curr_d >= next_d:
            deploy.popleft()
            cnt += 1
            
        else:
            curr_d = deploy.popleft()
            answer.append(cnt)
            cnt = 1
            
    answer.append(cnt)
        
    return answer