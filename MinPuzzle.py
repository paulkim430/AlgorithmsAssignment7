from collections import deque


def minEffort(puzzle):
    rows, cols = len(puzzle), len(puzzle[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Initialize a 2D array to track moves
    moves = [[float('inf')] * cols for _ in range(rows)]
    moves[0][0] = 0

    queue = deque([(0, 0)])

    while queue:
        row, col = queue.popleft()

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols:
                new_move = max(moves[row][col], abs(puzzle[new_row][new_col] - puzzle[row][col]))

                if new_move < moves[new_row][new_col]:
                    moves[new_row][new_col] = new_move
                    queue.append((new_row, new_col))

    return moves[rows - 1][cols - 1]
