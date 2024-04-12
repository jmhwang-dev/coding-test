import heapq
def get_min_compare(deck=[10, 21, 22, 30, 23, 32]):
    deck.sort()
    compare_count = 0
    while True:
        if len(deck) == 1:
            return 0

        if len(deck) == 2:
            return compare_count + sum(deck)

        value1 = heapq.heappop(deck)
        value2 = heapq.heappop(deck)
        compare_count += value1 + value2
        heapq.heappush(deck, value1 + value2)

N = int(input())
deck = [int(input()) for _ in range(N)]
print(get_min_compare(deck))