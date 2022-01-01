from typing import Set


def problem1(data):
    result = 0
    for row in data:
        for display in row:
            number_of_wires = len(display)
            if (number_of_wires > 1 and number_of_wires < 5) or number_of_wires == 7:
                result += 1
    return result

def problem2(result_part, decode_part):
    result = 0
    for row in range(len(decode_part)):
        current_row = decode_part[row]
        current_row.sort(key=lambda x: len(x))
        current_row = list(map(lambda x: set(x),current_row))
        # Decode wire mess
        wire_map = {}

        # finding from 7 and 1
        wire_map['a'] = current_row[1] - current_row[0]

        # find g & c from 5
        for chars in current_row[3:6]:
            if len(chars.intersection(current_row[2] - current_row[0])) == 2:
                wire_map['g'] = chars - current_row[2] - current_row[0]-wire_map['a']
                wire_map['c'] = current_row[0] - chars


        # find e from 10 and 9
        nine = current_row[2].union(wire_map['a'], wire_map['g'])
        wire_map['e'] = current_row[9] - nine

        # find f from 1
        wire_map['f'] = current_row[0] - wire_map['c']

        # find d from 3
        three = current_row[1].union(wire_map['g'])
        for chars in current_row[3:6]:
            if len(chars - three) == 1:
                wire_map['d'] = chars - three
                break

        # find b in 4
        wire_map['b'] = current_row[2] - current_row[0] - wire_map['d']


        # Use mapping to get output
        current_row = result_part[row]


        # Reverse to map from actual to correct mapping
        wire_map = {min(v): k for k, v in wire_map.items()}

        temp_result = 0
        for i in range(4):
            current_row[i] = list(map(lambda x: min(wire_map[x]),current_row[i]))
            current_row[i].sort(key=ord)

            value = 0
            match (current_row[i]):
                case ['a','b','c','e','f','g']:
                    value = 0
                case ['c','f']:
                    value = 1
                case ['a','c','d','e','g']:
                    value = 2
                case ['a','c','d','f','g']:
                    value = 3
                case ['b','c','d','f']:
                    value = 4
                case ['a','b','d','f','g']:
                    value = 5
                case ['a','b','d','e','f','g']:
                    value = 6
                case ['a','c','f']:
                    value = 7
                case ['a','b','c','d','e','f','g']:
                    value = 8
                case ['a','b','c','d','f','g']:
                    value = 9
                case _:
                    raise ValueError("Invalid input")
            temp_result += value * pow(10,3-i)
        result += temp_result
    return result


def main(data,_):
    parsedInput = list(map(lambda x: x.split('|'), data))
    decode_part = list(map(lambda x: x[0].split(),parsedInput))
    result_part = list(map(lambda x: x[1].split(),parsedInput))
    print(f"Problem 1: {problem1(result_part)}")
    print(f"Problem 2: {problem2(result_part, decode_part)}")

def test_problem1():
    assert problem1([['fdgacbe', 'cefdb', 'cefbgd', 'gcbe'], ['fcgedb', 'cgb', 'dgebacf', 'gc'], ['cg', 'cg', 'fdcagb', 'cbg'], ['efabcd', 'cedba', 'gadfec', 'cb'], ['gecf', 'egdcabf', 'bgf', 'bfgea'], ['gebdcfa', 'ecba', 'ca', 'fadegcb'], ['cefg', 'dcbef', 'fcge', 'gbcadfe'], ['ed', 'bcgafe', 'cdgba', 'cbgef'], ['gbdfcae', 'bgc', 'cg', 'cgb'], ['fgae', 'cfgab', 'fg', 'bagce']]) == 26

def test_problem2():
    data = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |fgae cfgab fg bagce""".split('\n')
    parsedInput = list(map(lambda x: x.split('|'), data))
    decode_part = list(map(lambda x: x[0].split(),parsedInput))
    result_part = list(map(lambda x: x[1].split(),parsedInput))
    assert problem2(result_part,decode_part) == 61229


