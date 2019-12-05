def digits(n):
    while n > 0:
        yield n % 10
        n //= 10

count = 0

for i in range(246540, 787420):
    d = list(digits(i))
    dp = list(zip(d, d[1:]))
    has_dup = False
    is_sorted = True

    for d1, d2 in dp:
        if d1 < d2:
            is_sorted = False
        elif d1 == d2:
            has_dup = True

    if has_dup and is_sorted:
        count += 1

print(count)