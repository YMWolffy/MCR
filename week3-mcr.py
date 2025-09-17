def is_win(game):
    win = False
    # Check rows
    if game[0][0] == game[0][1] == game[0][2] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[1][0] == game[1][1] == game[1][2] and (game[1][0] == 'X' or game[1][0] == 'O'):
        win = True
    if game[2][0] == game[2][1] == game[2][2] and (game[2][0] == 'X' or game[2][0] == 'O'):
        win = True
    # Check columns
    if game[0][0] == game[1][0] == game[2][0] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[0][1] == game[1][1] == game[2][1] and (game[0][1] == 'X' or game[0][1] == 'O'):
        win = True
    if game[0][2] == game[1][2] == game[2][2] and (game[0][2] == 'X' or game[0][2] == 'O'):
        win = True
    # Check diagonals
    if game[0][0] == game[1][1] == game[2][2] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[0][2] == game[1][1] == game[2][0] and (game[0][2] == 'X' or game[0][2] == 'O'):
        win = True
    return win

def main():
    game = [[' ' for _ in range(3)] for _ in range(3)]  # Tic-tac-toe board
    player1 = 'X'
    player2 = 'O'
    # 修改 1: 将 turn 的初始值从 False 改为 True
    # 你的原代码中, 循环一上来就执行 turn = not turn, 这会导致玩家2('O')先手。
    # 将初始值改为True, 第一次执行 not turn 后就会变为 False, 从而让玩家1('X')先手。
    turn = True  # False for player 1's turn, True for player 2's turn. Player 1 first.
    print("X = Player 1")
    print("O = Player 2")
    for n in range(9):
        turn = not turn  # Switch turns
        if not turn:
            print("Player 1: ", end="")
        else:
            print("Player 2: ", end="")
        print("Which cell to mark? i:[1..3], j:[1..3]: ")
        while True:
            i, j = map(int, input().split())
            i -= 1
            j -= 1
            # 检查坐标是否在有效范围
            if not (0 <= i < 3 and 0 <= j < 3):
                print("坐标必须在1-3范围内，请重新输入：")
                continue
            # 检查单元格是否已被占用
            if game[i][j] != ' ':
                print("该单元格已被占用，请重新输入：")
                continue
            break
        if not turn:
            game[i][j] = 'X'
        else:
            game[i][j] = 'O'
        # 将打印棋盘的步骤提前
        # 这样可以在宣布获胜或平局时, 显示出最后一步棋的盘面。
        for row in game:
            print(" ".join(row))
        if is_win(game):
            print("Win!")
            break  # Terminate the game
        if n == 8:  # All cells have been filled
            print("Tie!")
        # Show the game board
        

if __name__ == "__main__":
    main()
