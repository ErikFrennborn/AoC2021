def checkBoard(board, next_number):
    global boards_status, boards
    match = False
    for row in range(len(boards[0])):
        for col in range(len(boards[0][0])):
            if boards[board][row][col] == next_number:
                boards_status[board][row][col] = True

                # check if won
                part_match= [True, True]
                for x in range(5):
                    part_match[0] &= boards_status[board][row][x]
                for y in range(5):
                    part_match[1] &= boards_status[board][y][col]

                if part_match[0] or part_match[1]:
                    return True

    return False

def problem1(draw, boards):
    global boards_status
    boards_status = [[[False for _ in range(5)] for _ in range(5)] for _ in range(len(boards))]

    for next_number in draw:
        for board in range(len(boards)):

            # Did we win?
            if checkBoard(board, next_number):
                # Calute output
                part_sum = 0
                for row in range(5):
                    for col in range(5):
                        if not boards_status[board][row][col]:
                            part_sum += boards[board][row][col]
                return part_sum* next_number

    return -1

def problem2(draw, boards):
    remaining_boards = [i for i in range(len(boards))]
    global boards_status
    boards_status = [[[False for _ in range(5)] for _ in range(5)] for _ in range(len(boards))]

    for next_number in draw:
        for board in range(len(boards)):
            if not board in remaining_boards:
                continue

            # Did we win?
            if checkBoard(board, next_number):
                # The last win
                if len(remaining_boards) == 1:
                    # Calute output
                    part_sum = 0
                    for row in range(5):
                        for col in range(5):
                            if not boards_status[board][row][col]:
                                part_sum += boards[board][row][col]
                    return part_sum* next_number
                remaining_boards = list(filter(lambda x: x != board, remaining_boards))

    return -1



def parseInput(data):
    draw = list(map(int,data[0].split(',')))
    data = data[1:]

    boards = []
    for index in range(round(len(data)/6)):
        board = []
        for row in data[index*6 +1: index*6 + 6]:
            board.append(list(map(int,row.strip().split())))
        boards.append(board)
    return (draw, boards)

def main(data,_):
    global boards
    (draw, boards) = parseInput(data)
   #   for i in range(len(boards)):
        #  print(f"board: {i}")
        #  for j in range(5):
        #      print(boards[i][j])
#

    print(f"Problem 1: {problem1(draw, boards)}")
    print(f"Problem 2: {problem2(draw, boards)}")

def test_problem1():

    global boards
    data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
""".split('\n')
    (draw, boards) = parseInput(data)
    assert problem1(draw, boards) ==4512


def test_problem2():
    data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
""".split('\n')
    (draw, boards) = parseInput(data)
    assert problem2(draw,boards) == 1924
