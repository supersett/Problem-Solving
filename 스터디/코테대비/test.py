from itertools import permutations

dataset = ['A', 'B', 'C']

res = list(permutations(dataset, 3))

for x in res:
    print(x[0])
    print(x[1])
    print(x[2])