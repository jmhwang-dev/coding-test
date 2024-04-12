def get_min_value(N=4, distances=[2,3,1], prices=[5,2,4,1]):
    cur_price = prices[0]
    total_min_sum = cur_price * distances[0]
    for i, price in enumerate(prices[1:N-1]):
        if cur_price > price:
            cur_price = price

        total_min_sum += cur_price * distances[i+1]

    return total_min_sum

if __name__=="__main__":
    N = int(input())
    distances = list(map(int, input().split(' ')))
    prices = list(map(int, input().split(' ')))
    print(get_min_value(N, distances, prices))