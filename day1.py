def problem1(data):
    count = 0
    for i in range(1,len(data)):
        if data[i-1] < data[i]:
            count += 1

    return count

def problem2(data):
    count = 0
    temp = []
    for i in range(len(data)-2):
        temp.append(sum(data[i:i+3]))

    for i in range(1,len(temp)):
        if temp[i-1] < temp[i]:
            count += 1
    return count

def main(_,data):
    print(f"Problem 1: {problem1(data)}")
    print(f"Problem 2: {problem2(data)}")

def test_problem1():
    assert problem1([199,200,208,210,200,207,240,269,260,263]) == 7


def test_problem2():
    assert problem2([199,200,208,210,200,207,240,269,260,263]) == 5
