from math import ceil

def problem(data):
    result = [0,0]
    char_LUTs =  {'>':'<', ')':'(', ']':'[', '}':'{'}
    points_LUTs = {'>':25137, ')':3, ']':57, '}':1197}

    partial_result = []
    for line in data:
        corrupted_line = False
        stack = []
        for char in line.strip():
            if char in ['<', '(', '[', '{']:
                stack.append(char)
            elif char in char_LUTs:
                if stack.pop() != char_LUTs[char]:
                    result[0] += points_LUTs[char]
                    corrupted_line = True
                    break
            else:
                raise ValueError(f"'{char}' is not a value input")

        if corrupted_line:
            continue
        rest_LUTs = {'(':1, '[':2, '{':3, '<':4}

        score = 0
        for _ in range(len(stack)):
            char = stack.pop()
            score *= 5
            score += rest_LUTs[char]

        partial_result.append(score)

    partial_result.sort()
    result_size = len(partial_result)
    result[1] = partial_result[int(result_size/2)]
    return result

def main(data,_):
    result = problem(data)
    print(f"Problem 1: {result[0]}")
    print(f"Problem 2: {result[1]}")

def test_problem1():
    data = """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".split('\n')
    assert problem(data)[0] == 26397

def test_problem2():
    data = """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".split('\n')
    assert problem(data)[1]== 288957

