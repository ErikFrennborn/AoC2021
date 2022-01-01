def problem(lines, max_x, max_y, problem2):
    grid = [[ 0 for _ in range(max_x + 1)] for _ in range(max_y +1 )]

    # Population grid
    for line in lines:
        delta_x = line.end.x - line.start.x
        delta_y = line.end.y - line.start.y

        length = abs(delta_x) if delta_x != 0 else abs(delta_y)
        length += 1
        step_x = 0 if delta_x == 0 else int(delta_x/abs(delta_x))
        step_y = 0 if delta_y == 0 else int(delta_y/abs(delta_y))
        # Diagonal
        if not problem2:
            if (line.start.x - line.end.x != 0) and (line.start.y - line.end.y != 0):
                continue
        x = line.start.x
        y = line.start.y
        for _ in range(length):
            grid[y][x] += 1
            x += step_x
            y += step_y

    # Get result
    count = 0
    for row in grid:
        for value in row:
            count += int(value > 1)

    return count

class Coord:
    x: int
    y: int

    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"{self.x}:{self.y}"

class Line:
    start: Coord
    end: Coord
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def __repr__(self) -> str:
        return f"{self.start} -> {self.end}"

def parseCoord(item):
    coords = list(map(int,item.split(",")))
    return Coord(*coords)

def parseInput(data):
    max_x = 0
    max_y = 0
    lines = []
    for line in data:
        strings = line.split()
        points = [strings[0], strings[2]]
        coords = list(map(parseCoord,points))
        for i in range(2):
            max_x =  max_x if max_x > coords[i].x else coords[i].x
            max_y =  max_y if max_y > coords[i].y else coords[i].y
        lines.append(Line(*coords))
    return (lines, max_x, max_y)

def main(data,_):
    print(f"Problem 1: {problem(*parseInput(data), False)}")
    print(f"Problem 2: {problem(*parseInput(data),True)}")

def test_problem1():
    data = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".split("\n")

    assert problem(*parseInput(data),False) == 5

def test_problem2():
    data = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".split("\n")

    assert problem(*parseInput(data),True) == 12
