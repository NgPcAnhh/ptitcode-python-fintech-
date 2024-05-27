for i in range(int(input())):
    n = int(input())
    if n % 2 != 0: #lẻ
        day_so_chan = [1/(2*i + 1) for i in range(0,int(n/2)+1)]
        a = sum(day_so_chan)
        b = format(a,'.6f')
        print(b)
    else: #chẵn 
        day_so_le = [1/(2*i) for i in range(1,int(n/2)+1)]
        c = sum(day_so_le)
        d = format(c, '.6f')
        print(d)