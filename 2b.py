# 📍 Программа для игры с конфетами человек против человека реализованная в терминале. 
# Игроки ходят друг за другом, вписывая желаемое количество конфет. 
# Первый ход определяется жеребьёвкой. В конце выводится игрок, который победил. 
#
# Условие задачи: На столе лежит 221 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
#
# В качестве дополнительного усложнения можно:
#   a) Добавить игру против бота ( где бот берет рандомное количество конфет от 0 до 28)
#   b) Подумать как наделить бота "интеллектом" 
#   (есть алгоритм, позволяющий выяснить какое количество конфет необходимо брать, 
#   чтобы гарантированно победить, соответственно внедрить этот алгоритм боту.)

# Вариант "человек против умного бота":

from random import randint

def candy_take(player_name):
    x = int(input(f'🗣  {player_name}, введите количество конфет, которое хотите взять (от 1 до 28): ✏️ '))
    while x < 1 or x > 28:
        x = int(input('❌ Введено неверное количество конфет, попробуйте ещё раз: ✏️  '))
    return x

def print_turn_res(player_name, k, counter, value):
    print(f'❗️{player_name} взял {k} 🍬, теперь у него имеется {counter} 🍬')
    print(f'На столе теперь {value} 🍬')

def bot_ai(value):
    k = 28
    if value-k <= 28 and value >= 28: # and k > 0:
        k = value-29
    return k

player1 = input('✏️  Введите имя игрока: ')
player2 = 'Бот'
value = 221
priority = randint(0, 2)
if priority:
    print(f'🎲 По итогам жеребьёвки первым ходит игрок по имени {player1}!')
else:
    print(f'🎲 По итогам жеребьёвки первым ходит {player2}!')

print(f'На столе находится {value} 🍬')

counter1 = 0
counter2 = 0

while value > 28:
    if priority:
        k = candy_take(player1)
        counter1 += k
        value -= k
        priority = False
        if value > 29:
            print_turn_res(player1, k, counter1, value)
        else:
            priority = True
            break    
    else:
        k = bot_ai(value)
        counter2 += k
        value -= k
        priority = True
        if value > 29:
            print_turn_res(player2, k, counter2, value)
        else:
            break  

if priority:
    print(f'🎉 Выиграл игрок по имени {player1}!')
else:
    print(f'🎉 Выиграл {player2}!')