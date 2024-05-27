for i in range(int(input())):
    n = input()
    s = set()
    l = []
    for char in n:
        if char.isalpha():  # Kiểm tra xem ký tự có phải là chữ cái hay không
            l.append(char)
            s.add(char)
    l.sort()
    result = ''.join(l) + str(len(s))  # Nối các phần tử trong l và len(s) thành một chuỗi
    print(result)
