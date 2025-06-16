def get_changes_count(pay=380):
    remain = 1000 - pay
    count = 0
    for changes in [500, 100, 50, 10, 5, 1]:
        count += remain // changes
        remain = remain % changes
    return count

N = int(input())
print(get_changes_count(N))