import sys

expression = sys.stdin.readline().split('-')

partial_sum = []
for t in expression:
    temp = list(map(int, t.split('+')))
    partial_sum.append(sum(temp))

total = partial_sum[0]
for psum in partial_sum[1:]:
    total -= psum

print(total)