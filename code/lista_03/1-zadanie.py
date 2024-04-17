def gen_pos_num(start=1, end=float('inf')):
    while start <= end:
        yield start
        start += 1


def gen_sq():
    for i in gen_pos_num():
        yield i ** 2


def select(iterable, n):
    it = iter(iterable)
    L = []
    try:
        for i in range(n):
            L.append(next(it))
    except StopIteration:
        return L
    else:
        return L


#     g = gen_pos_num()
# print(next(g))
# print(next(g))
# print(next(g))
# print(select(gen_pos_num(), 10))
# print(select(gen_sq(), 10))

t = ((a, b, c) for c in gen_pos_num(start=3) for b in gen_pos_num(end=c - 1) for a in gen_pos_num(end=b - 1) if
     a ** 2 + b ** 2 == c ** 2)

print(select(t, 10))
