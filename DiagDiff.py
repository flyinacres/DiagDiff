__author__ = 'rfischer'

N = input()

diff = 0
for i in range(0, N):
    row = [int(n) for n in raw_input().split(' ')]
    diff += row[i] - row[N-1-i]

print abs(diff)