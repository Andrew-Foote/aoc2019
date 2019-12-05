def digits(n):
    while n > 0:
        yield n % 10
        n //= 10

def repeat_counts(ls):
    result = {}
    cur_i = 0
    count = 1

    for nxt_i, nxt in enumerate(ls[1:], start=1):
        if nxt == ls[cur_i]:
            count += 1
        else:
            result[cur_i] = count
            cur_i = nxt_i
            count = 1

    result[cur_i] = count
    return result

count = 0

for i in range(246540, 787420):
    d = list(digits(i))

    if all(d1 >= d2 for d1, d2 in zip(d, d[1:])):
        if any(c == 2 for i, c in repeat_counts(d).items()):
            count += 1

print(count)