def how_many(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + 1 * i
    return sum

print(how_many(5000000))


def sum_bowls(n):
    if n == 1:
        return 1
    else:
        return sum_bowls(n-1) + n

print('Recursive sum: ' + str(sum_bowls(998)))
