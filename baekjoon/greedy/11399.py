def atm_time(N=5, times=[3,1,4,3,2]):
    _times = sorted(times)
    total_time = 0
    for i in range(N):
        total_time += sum(_times[:i+1])
    return total_time

if __name__=="__main__":
    N = int(input())
    times = list(map(int, input().split()))
    print(atm_time(N, times))