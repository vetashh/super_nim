import random
def start_game():
    letters_board = '   a  b  c  d  e  f  g  h'
    board = [[] for i in range(8)]
    print(letters_board)
    for ind_row in range(1, 9):
        for ind_col in range(8):
            board[ind_row-1].append(random.choice([0, 1]))
        print(ind_row, board[ind_row-1])
    step = 0

    def play(step):
        letters = 'abcdefgh'
        numbers = '12345678'
        while sum(row.count(1) for row in board) != 0:
            print()
            n = input(f'Игрок {step % 2 + 1}, введите координаты горизонтали или вертикали: \n')
            if (n not in letters and n not in numbers) or n == '':
                print('ОШИБКА! Введите корректные координаты!')
                print(play(step))
            elif n in letters:
                num_column = letters.index(n)
                for ind_row in range(8):
                    board[ind_row][num_column] = 0
            else:
                num_row = numbers.index(n)
                for ind_column in range(8):
                    board[num_row][ind_column] = 0
            step += 1
            print(letters_board)
            for ind in range(8):
                print(ind+1, board[ind])
        print(f'Победил игрок {(step - 1) % 2 + 1} \n')
    play(step)

    def end_game():
        new_game = input('Хотите начать новую игру? Введите \"Да\" или \"Нет\": \n')
        if new_game.lower() == 'да':
            start_game()
        elif new_game.lower() == 'нет':
            return
        else:
            print('Введите корректный ответ \n')
            end_game()
    end_game()
start_game()
