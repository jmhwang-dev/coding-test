def word_math(words=["GCF", "ACDEB"]):
    values = {}
    for word in words:
        digits = len(word) - 1
        for w in word:
            if not w in values.keys():
                values[w] = 10 ** digits
            else:
                values[w] += 10 ** digits
            digits -= 1
    
    output = sorted(values.items(), key=lambda x: x[1], reverse=True)
    total = 0
    start = 9
    for _, num in output:
        total += num * start
        start -= 1

    return total
    
N = int(input())
words = [input() for _ in range(N)]
print(word_math(words))