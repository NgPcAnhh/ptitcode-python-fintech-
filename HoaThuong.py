a = input()
lower = 0 
for i in a:
    if i.islower():
        lower = lower + 1
   
if lower >= len(a) - lower:
         print(a.lower())
else: 
    if lower <= len(a) - lower:
        print(a.upper())

