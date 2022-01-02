def problem(init_state, NUMBER_OF_DAY):
    CYCLES = 7
    NEW_FISH_PENALY = 2
    state = [0 for _ in range(CYCLES + NEW_FISH_PENALY)]
    # init
    for fish in init_state:
        state[fish] += 1

    # tick
    for _ in range(NUMBER_OF_DAY):
        number_of_fishs_to_dived = state.pop(0)
        state[6] += number_of_fishs_to_dived
        # create new fishs
        state.append(number_of_fishs_to_dived)

    result = 0
    for i in range(CYCLES+NEW_FISH_PENALY):
        result += state[i]
    return result

def main(data,_):
    parsedInput = list(map(int,data[0].strip().split(',')))
    print(f"Problem 1: {problem(parsedInput,80)}")
    print(f"Problem 2: {problem(parsedInput,256)}")

def test_problem1():
    assert problem([3,4,3,1,2], 80) == 5934

def test_problem2():
    assert problem([3,4,3,1,2], 256) == 26984457539
