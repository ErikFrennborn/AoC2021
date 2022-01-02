def problem1(data):
    x = y = 0
    for line in data:
        match line.split():
            case ["forward", dist]:
                x += int(dist)
            case ["up", dist]:
                y -= int(dist)
            case ["down", dist]:
                y += int(dist)
            case _:
                raise ValueError("Invalided input: "+ line)
    return x*y

def problem2(data):
    x = y = 0
    aim = 0
    for line in data:
        match line.split():
            case ["forward", dist]:
                y += aim*int(dist)
                x += int(dist)
            case ["up", dist]:
                aim -= int(dist)
            case ["down", dist]:
                aim += int(dist)
            case _:
                raise ValueError("Invalided input: "+ line)
    return x*y

def main(data_raw,_):
    print(f"Problem 1: {problem1(data_raw)}")
    print(f"Problem 2: {problem2(data_raw)}")

def test_problem1():
    assert(problem1("""forward 5
down 5
forward 8
up 3
down 8
forward 2""".split('\n')) == 150)

def test_problem2():
    assert(problem2("""forward 5
down 5
forward 8
up 3
down 8
forward 2""".split('\n')) == 900)
