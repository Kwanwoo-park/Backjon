from collections import Counter
from sys import stdin

n = int(stdin.readline())
num = list(map(int, stdin.readline().split()))
counter = Counter(num)
result = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and counter[num[stack[-1]]] < counter[num[i]]:
        result[stack.pop()] = num[i]
    stack.append(i)

print(*result)