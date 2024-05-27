P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

inputs = []
while True:
    str = input()
    if str == "0":
        break
    inputs.append(str)

for a in inputs:
    k, s = a.split()
    k = int(k)
    result = ""
    for char in s:
        I = P.index(char)
        new_char = P[(I + k) % 28]
        result = new_char + result
    print(result)
