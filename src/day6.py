def problem(init_state, NUMBER_OF_DAY):
    state = init_state
    # tick
    CYCLES = 6
    NEW_FISH_PENALY = 2
    for _ in range(NUMBER_OF_DAY):
        next_state = []
        new_fishs = []
        for fish in state:
            if fish == 0:
                # create new fish
                new_fishs.append(CYCLES + NEW_FISH_PENALY)
                next_state.append(CYCLES)
            else:
                next_state.append(fish-1)
        state = next_state + new_fishs
    return len(state)

def main(data,_):
    parsedInput = list(map(int,data[0].strip().split(',')))
    print(f"Problem 1: {problem(parsedInput,80)}")
    print(f"Problem 2: {problem(parsedInput,256)}")

def test_problem1():
    assert problem([3,4,3,1,2], 80) == 5934

def test_problem2():
    assert problem([3,4,3,1,2], 256) == 26984457539
