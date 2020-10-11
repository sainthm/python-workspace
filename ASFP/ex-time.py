def convert_seconds(arg):
    if arg < 60:
        return str(arg) + " 초 "
    
    minutes = arg // 60
    seconds = arg % 60
    if minutes < 60:
        return str(minutes) + " 분 " + str(seconds) + " 초 "
    
    hours = minutes // 60
    minutes = minutes % 60
    return str(hours) + " 시간 " + str(minutes) + " 분 " + str(seconds) + " 초 "

print(convert_seconds(3))
print(convert_seconds(60))
print(convert_seconds(323))
print(convert_seconds(60 * 60 + 323 * 2))