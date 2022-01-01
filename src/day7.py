def problem1(data):
    lowest_fuel_usage = None
    for target in range(max(data)):
        fuel_usage = sum(map(lambda x: abs(x-target),data))
        if lowest_fuel_usage == None or lowest_fuel_usage > fuel_usage:
            lowest_fuel_usage = fuel_usage
    return lowest_fuel_usage

def fuelCost(n):
    return int(n*(n+1)/2)

def problem2(data):
    lowest_fuel_usage = None
    for target in range(max(data)):
        fuel_usage = sum(map(lambda x: fuelCost(abs(x-target)),data))
        if lowest_fuel_usage == None or lowest_fuel_usage > fuel_usage:
            lowest_fuel_usage = fuel_usage
    return lowest_fuel_usage

def main(data,_):
    parsedInput = list(map(int,data[0].strip().split(',')))
    print(f"Problem 1: {problem1(parsedInput)}")
    print(f"Problem 2: {problem2(parsedInput)}")

def test_problem1():
    assert problem1([16,1,2,0,4,2,7,1,2,14]) == 37

def test_problem2():
    assert problem2([16,1,2,0,4,2,7,1,2,14]) == 168

