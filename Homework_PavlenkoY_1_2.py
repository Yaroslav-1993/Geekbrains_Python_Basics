total_sec = int(input("Введите время в секундах >>>"))

hours = total_sec // 3600
minutes = total_sec % 3600 // 60
seconds = total_sec % 3600 % 60


print("%02d:%02d:%02d" % (hours, minutes, seconds))
