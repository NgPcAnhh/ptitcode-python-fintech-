import re
from itertools import groupby

s = int(input())
for i in range(s):
    n = input()
    result = [list(group) for key, group in groupby(n)]
    output = ''.join([str(len(i)) + i[0] for i in result])
    print(output)
