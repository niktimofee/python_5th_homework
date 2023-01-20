# 📍 RLE алгоритм: модуль сжатия и восстановления данных.
# Модуль сжатия для чисел:
#
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
#
# Модуль сжатия для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
#
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.

def coding(symbols):
    count = 1
    res = ''
    for i in range(len(symbols) - 1):
        if symbols[i] == symbols[i + 1]:
            count += 1
        else:
            res = res + str(count) + symbols[i]
            count = 1
    if count > 1 or (symbols[len(symbols) - 2] != symbols[-1]):
        res = res + str(count) + symbols[-1]
    return res

def decoding(symbols):
    count = ''
    res = ''
    for i in range(len(symbols)):
        if not symbols[i].isalpha():
            count += symbols[i]
        else:
            res = res + symbols[i] * int(count)
            count = ''
    return res

s = input("Введите символы для сжатия: ")
print(f"Символы после сжатия: {coding(s)}")
print(f"Символы после восстановления: {decoding(coding(s))}")