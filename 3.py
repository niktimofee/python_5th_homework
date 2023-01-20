# 📍 Программа для игры в "Крестики-нолики". 
# Игра реализуется в терминале, игроки ходят поочередно. 
# Также необходимо вывести карту (как удобнее, можно например в виде списка, 
# внутри которого будут 3 списка по 3 элемента, 
# каждый из которого обозначает соответсвующие клетки от 1 до 9) и 
# сделать проверку не занята ли клетка, на которую мы хотим поставить крестик или нолик, 
# и проверку на победу (стоят ли крестики или нолики в ряд по диагонали, вертикали или горизонтали.)

board = list(range(1,10))

def draw_board(board):
    print ('-' * 13)
    for i in range(3):
        print ('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
        print ('-' * 13)

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input(f'Введите номер клетки чтобы поставить "{player_token}" : ')
        try:
            player_answer = int(player_answer)
        except:
            print ('Введено не число!')
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "xo"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print ('Эта клетка уже занята!')
        else:
            print ('Введено неверное число! Введите число от 1 до 9 чтобы сделать ход.')

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input('x')
        else:
            take_input('o')
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (f'Победил {tmp}!')
                win = True
                break
        if counter == 9:
            print ('Ничья!')
            break
    draw_board(board)

main(board)