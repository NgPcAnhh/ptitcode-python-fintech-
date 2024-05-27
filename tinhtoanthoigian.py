from datetime import datetime

# Tạo một danh sách để lưu trữ thông tin về các game
games = []

# Nhập thông tin về các game
for _ in range(int(input())):
    # bước nhập input
    magamer = input()
    tengamer = input()
    n = input()
    m = input()

    # xử lý thời gian
    t_in = datetime.strptime(n, '%H:%M')
    t_out = datetime.strptime(m, '%H:%M')

    # tính toán thời gian giữa hai mốc 
    diff = t_out - t_in

    # Lấy số giờ và phút từ thời gian chênh lệch
    hours, remainder = divmod(diff.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    # Lưu kết quả vào biến c với định dạng mong muốn
    tg = f'{hours} gio {minutes} phut'

    # Thêm thông tin về game vào danh sách
    games.append((magamer, tengamer, tg, diff))

# Sắp xếp danh sách game theo thời gian chơi giảm dần
games.sort(key=lambda x: x[3], reverse=True)

# In thông tin về các game
for game in games:
    print(game[0], game[1], game[2])
