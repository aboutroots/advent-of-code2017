def find_start_x(maze):
    for i in range(len(maze[0])):
        if maze[0][i] == '|':
            return i


def find_direction(prev_direction, position, maze, moves):
    direction = ['left', 'right']
    for d in [0, 1]:
        if prev_direction != moves[direction[1 - d]]:
            new_pos = [sum(x) for x in zip(position, moves[direction[d]])]
            constraint1 = 0 < new_pos[0] < len(maze)
            constraint2 = 0 < new_pos[1] < len(maze[new_pos[0]])
            if constraint1 and constraint2:
                new_tile = maze[new_pos[0]][new_pos[1]]
                if new_tile == '-' or new_tile.isalpha():
                    return moves[direction[d]]

    direction = ['up', 'down']
    for d in [0, 1]:
        if prev_direction != moves[direction[1 - d]]:
            new_pos = [sum(x) for x in zip(position, moves[direction[d]])]
            constraint1 = 0 < new_pos[0] < len(maze)
            constraint2 = 0 < new_pos[1] < len(maze[new_pos[0]])
            if constraint1 and constraint2:
                new_tile = maze[new_pos[0]][new_pos[1]]
                if new_tile == '|' or new_tile.isalpha():
                    return moves[direction[d]]

if __name__ == '__main__':
    with open("day19.txt") as file:
        board = [line.rstrip('\n') for line in file.readlines()]
    moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    pos = [0, find_start_x(board)]      # (y, x) !!!!!!
    mov = moves['down']
    found = False
    backpack = []
    steps = 0

    while not board[pos[0]][pos[1]].isspace():
        steps += 1
        if board[pos[0]][pos[1]].isalpha():
            backpack.append(board[pos[0]][pos[1]])

        pos = [sum(x) for x in zip(pos, mov)]
        if board[pos[0]][pos[1]] == '+':
            mov = find_direction(mov, pos, board, moves)
            pos = [sum(x) for x in zip(pos, mov)]
            steps += 1

    print("".join(backpack), steps)