import time

def is_valid_move(x, y, board, N):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def brute_force_knight_tour_util(x, y, move_count, board, x_moves, y_moves, N):
    if move_count == N * N:
        return True

    for k in range(8):
        next_x = x + x_moves[k]
        next_y = y + y_moves[k]
        if is_valid_move(next_x, next_y, board, N):
            board[next_x][next_y] = move_count
            if brute_force_knight_tour_util(next_x, next_y, move_count + 1, board, x_moves, y_moves, N):
                return True
            board[next_x][next_y] = -1
    return False

def brute_force_knight_tour(N):
    board = [[-1 for _ in range(N)] for _ in range(N)]
    x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
    y_moves = [1, 2, 2, 1, -1, -2, -2, -1]
    board[0][0] = 0
    if brute_force_knight_tour_util(0, 0, 1, board, x_moves, y_moves, N):
        return board
    else:
        return None

def get_degree(x, y, board, N, x_moves, y_moves):
    count = 0
    for i in range(8):
        new_x = x + x_moves[i]
        new_y = y + y_moves[i]
        if is_valid_move(new_x, new_y, board, N):
            count += 1
    return count

def warnsdorff_knight_tour_util(x, y, move_count, board, x_moves, y_moves, N):
    if move_count == N * N:
        return True
    next_moves = []
    for i in range(8):
        new_x = x + x_moves[i]
        new_y = y + y_moves[i]
        if is_valid_move(new_x, new_y, board, N):
            degree = get_degree(new_x, new_y, board, N, x_moves, y_moves)
            next_moves.append((degree, new_x, new_y))
    next_moves.sort(key=lambda item: item[0])
    
    for _, new_x, new_y in next_moves:
        board[new_x][new_y] = move_count
        if warnsdorff_knight_tour_util(new_x, new_y, move_count + 1, board, x_moves, y_moves, N):
            return True
        board[new_x][new_y] = -1
    return False

def warnsdorff_knight_tour(N):
    board = [[-1 for _ in range(N)] for _ in range(N)]
    x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
    y_moves = [1, 2, 2, 1, -1, -2, -2, -1]
    board[0][0] = 0
    if warnsdorff_knight_tour_util(0, 0, 1, board, x_moves, y_moves, N):
        return board
    else:
        return None

def print_board(board):
    if board:
        for row in board:
            print(' '.join(f"{cell:2}" for cell in row))
    else:
        print("Nenhuma solução encontrada.")

if __name__ == "__main__":
    sizes = [5, 8, 10]
    
    for N in sizes:
        print(f"\nTabuleiro {N}x{N} - Força Bruta:")
        start = time.time()
        board_brute = brute_force_knight_tour(N)
        end = time.time()
        print_board(board_brute)
        print(f"Tempo: {end - start:.4f} segundos")
        
        print(f"\nTabuleiro {N}x{N} - Heurística de Warnsdorff:")
        start = time.time()
        board_warnsdorff = warnsdorff_knight_tour(N)
        end = time.time()
        print_board(board_warnsdorff)
        print(f"Tempo: {end - start:.4f} segundos")
