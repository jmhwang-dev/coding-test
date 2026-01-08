def solution(sizes):
    answer = 0
    
    max_height = 1
    max_width = 1
    for size in sizes[:]:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]
            
        max_height = max(max_height, size[0])
        max_width = max(max_width, size[1])
        
    answer = max_width * max_height
    return answer