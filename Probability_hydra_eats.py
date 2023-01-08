from random import randint
n = 10000
cnt = 100
choice = [0] * cnt


for _ in range(n):
    ls = list(range(cnt))
    while len(ls) > 2:
        r = randint(0, 2)
        choice[ls[r]] += 1
        ls = ls[r+1:]

per_0 = [0, 0]
for ni, i in enumerate(choice):
    per = round(i / n * 100, 2)
    if per > per_0[1]:
        per_0 = [ni, per]
    print(f'{ni}: {per} %')


print('max position {}: at {} %'.format(*per_0))
