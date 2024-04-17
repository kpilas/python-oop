class Fibo:
    def __init__(self, n):
        self.f0 = 0
        self.f1 = 1
        self.n = n

    def __next__(self):
        self.f0, self.f1 = self.f1, self.f0 + self.f1
        if self.f0 < self.n:
            return self.f0
        else:
            raise StopIteration

    def __iter__(self):
        return self


def fibo(n=float('inf')):
    f0, f1 = 0, 1
    while True:
        f0, f1 = f1, f0 + f1
        if f0 < n:
            yield f0
        else:
            return


f = Fibo(1000)
f2 = fibo()

# for i in f:
#     print(i)
#
# for i in f2:
#     print(i)

from itertools import islice
for i in islice(f2, 99999, 10009):
    print(i)
