import re

s = int(input())
for i in range(s):
    n = input()
    pairs = re.findall(r'([A-Za-z])(\d)', n)
    pairs = [[i[0], int(i[1])] for i in pairs]

    result = '' 
#lưu kết quả vào string
    for pair in pairs:
        result += pair[0] * pair[1]

    print(result)
