s1 = input() # nhập string ban đầu
s2 = input() # string để chèn
n = int(input())
m = n-1

s1 = s1[:m] + s2 + s1[m:]
print(s1)
