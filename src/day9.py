from functools import reduce

def lowestPoints(data):
    y_length = len(data)
    x_length = len(data[0])
    result = []
    for y in range(y_length):
        for x in range(x_length):
            lowest = [True for _ in range(4)]
            lowest[0] = data[y][x] < data [y][x-1] if x > 0 else True
            lowest[1] = data[y][x] < data [y][x+1] if x < x_length -1 else True
            lowest[2] = data[y][x] < data [y-1][x] if y > 0  else True
            lowest[3] = data[y][x] < data [y+1][x] if y < y_length -1 else True

            if all(lowest):
                result.append((x,y))
    return result

def problem1(data):
    result = 0
    for (x,y) in lowestPoints(data):
        result += data[y][x] + 1
    return result

def addToPoints(data, unique_point_in_basins, x,y):
    global point_to_check
    if (x,y) not in unique_point_in_basins and data[y][x] != 9:
        point_to_check.append((x,y))

def problem2(data):
    global point_to_check
    basins_size = []
    y_length = len(data)
    x_length = len(data[0])
    for point in lowestPoints(data):
        point_to_check = [point]
        unique_point_in_basins = set()
        while len(point_to_check) != 0:
            current_point = point_to_check.pop()
            (x,y) = current_point
            unique_point_in_basins.add(current_point)
            if x > 0:
                addToPoints(data,unique_point_in_basins,x-1,y)
            if x < x_length -1:
                addToPoints(data,unique_point_in_basins,x+1,y)
            if y > 0:
                addToPoints(data,unique_point_in_basins,x,y-1)
            if y < y_length -1:
                addToPoints(data,unique_point_in_basins,x,y+1)

        basins_size.append(len(unique_point_in_basins))

    basins_size.sort()
    return reduce(lambda x,y: x*y,basins_size[-3:])

def main(data,_):
    temp_data = []
    for row in data:
        temp_row = []
        for value in row.strip():
            temp_row.append(int(value))
        temp_data.append(temp_row)
    data = temp_data
    print(f"Problem 1: {problem1(data)}")
    print(f"Problem 2: {problem2(data)}")

def test_problem1():
    assert problem1([[2,1,9,9,9,4,3,2,1,0],
[3,9,8,7,8,9,4,9,2,1],
[9,8,5,6,7,8,9,8,9,2],
[8,7,6,7,8,9,6,7,8,9],
[9,8,9,9,9,6,5,6,7,8]]) == 15

def test_problem2():
    assert problem2([[2,1,9,9,9,4,3,2,1,0],
[3,9,8,7,8,9,4,9,2,1],
[9,8,5,6,7,8,9,8,9,2],
[8,7,6,7,8,9,6,7,8,9],
[9,8,9,9,9,6,5,6,7,8]]) == 1134

