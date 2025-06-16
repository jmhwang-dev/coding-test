def coin_0(coins=[1,5,10,50,100,500,1000,5000,10000,50000], K=4790):
    coins_desc = sorted(coins, reverse=True)
    _K = K
    count = 0

    for coin in coins_desc:
        count += int(_K / coin)
        _K = _K % coin

    return count

if __name__=="__main__":
    N, K = list(map(int, input().split()))
   
    coins = []
    for i in range(N):
        coins.append(int(input()))

    count = coin_0(coins, K)
    print(count)