def problem(input_data, number_of_steps):
    data = list(map(lambda x: x[:], input_data))
    flashes = 0
    y_length = len(data)
    x_length = len(data[0])
    all_flash = -1
    for time_step in range(number_of_steps):
        has_flashed = set()
        should_flash = set()

        # Simulate step
        for y in range(y_length):
            for x in range(x_length):
                data[y][x] += 1
                if data[y][x] > 9:
                    should_flash.add((x,y))
        # Flash
        zeros = set()
        while len(should_flash) != 0:
            (x,y) = should_flash.pop()
            zeros.add((x,y))
            has_flashed.add((x,y))
            flashes += 1
            for offset_y in range(3):
                true_y = y + offset_y -1
                if true_y < 0 or true_y >= y_length:
                    continue
                for offset_x in range(3):
                    true_x = x + offset_x -1
                    if true_x < 0 or true_x >= x_length:
                        continue
                    data[true_y][true_x] += 1

                    if (true_x,true_y) in has_flashed:
                        continue

                    if data[true_y][true_x] > 9:
                        should_flash.add((true_x, true_y))

        for (x,y) in zeros:
            data[y][x] = 0

        if len(zeros) == x_length*y_length:
            all_flash = time_step + 1
            break
    return (flashes,all_flash)

def main(data,_):
    parsedInput = []
    for line in data:
        parsedInput.append(list(map(int,line.strip())))
    print(f"Problem 1: {problem(parsedInput,100)[0]}")
    print(f"Problem 2: {problem(parsedInput,9999999)[1]}")

def test_problem1():
    assert problem([[5,4,8,3,1,4,3,2,2,3],
[2,7,4,5,8,5,4,7,1,1],
[5,2,6,4,5,5,6,1,7,3],
[6,1,4,1,3,3,6,1,4,6],
[6,3,5,7,3,8,5,4,7,8],
[4,1,6,7,5,2,4,6,4,5],
[2,1,7,6,8,4,1,7,2,1],
[6,8,8,2,8,8,1,1,3,4],
[4,8,4,6,8,4,8,5,5,4],
[5,2,8,3,7,5,1,5,2,6]],100)[0] == 1656

def test_problem2():
    assert problem([[5,4,8,3,1,4,3,2,2,3],
[2,7,4,5,8,5,4,7,1,1],
[5,2,6,4,5,5,6,1,7,3],
[6,1,4,1,3,3,6,1,4,6],
[6,3,5,7,3,8,5,4,7,8],
[4,1,6,7,5,2,4,6,4,5],
[2,1,7,6,8,4,1,7,2,1],
[6,8,8,2,8,8,1,1,3,4],
[4,8,4,6,8,4,8,5,5,4],
[5,2,8,3,7,5,1,5,2,6]],99999999999)[1] == 195
