def problem1(lines, max_x, max_y):
    grid = [[ 0 for _ in range(max_x + 1)] for _ in range(max_y +1 )]

    # Population grid
    for line in lines:
        # Diagonal
        if (line.start.x - line.end.x != 0) and (line.start.y - line.end.y != 0):
            continue
        reverse_x = line.start.x > line.end.x
        reverse_y = line.start.y > line.end.y

        for y in range(line.start.y, line.end.y + (-1 if reverse_y else 1), -1 if reverse_y else 1):
            for x in range(line.start.x, line.end.x +(-1 if reverse_x else 1), -1 if reverse_x else 1):
                grid[y][x] += 1

    # Get result
    count = 0
    for row in grid:
        for value in row:
            count += int(value > 1)

    return count

def problem2(data):
    count = 0
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
    (lines, max_x, max_y) = parseInput(data)
    print(f"Problem 1: {problem1(lines, max_x, max_y)}")
    print(f"Problem 2: {problem2(data)}")

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

    assert problem1(*parseInput(data)) == 5


#  def test_problem2():
#      assert problem2([199,200,208,210,200,207,240,269,260,263]) == 5
