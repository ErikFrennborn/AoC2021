def helperfunction(data):
    result = [0 for _ in range(len(data[0].strip()))]
    for line in data:
        for (i,c) in enumerate(line.strip()):
            if c == '1':
                result[i] += 1

    return result

def problem1(data):
    input_size = len(data)
    max_length = int('1'*(len(data[0].strip())),2)

    result = helperfunction(data)

    for i in range(len(result)):
        result[i] = 1 if result[i] >= input_size/2 else 0

    a = 0
    for (i,v) in enumerate(result[::-1]):
        a += v*pow(2,i)

    b = max_length - a
    return a*b

#  def filterfunction(line, truth, bais, input_size):
    #  if truth[0] == input_size/2:
    #      return int(line[1]) == bais
    #  else:
    #      if int(line[0]) == bais:
        #  return

def getFirst(values, index):
    ones = 0
    for value in values:
        ones += int(value[index] == '1')

    return ones


def problem2(in_data):
    result = 1
    for prop in range(2):
        data = in_data
        for index in range(len(data[0])):
            ones = getFirst(data,index)

            # Filter
            temp_data = []
            for x in data:
                if len(data) != 2*ones:
                    key = '1' if int(2*ones > len(data)) == prop else '0'
                else:
                    key = str(prop)

                if (x[index] == key ):
                    temp_data.append(x)
            data = temp_data

            if len(data) == 1:
                result *= int(data[0],2)
                break
    return result

def main(data,_):
    print(f"Problem 1: {problem1(data)}")
    print(f"Problem 2: {problem2(data)}")

def test_problem1():
    assert problem1(["00100",
"11110",
"10110",
"10111",
"10101",
"01111",
"00111",
"11100",
"10000",
"11001",
"00010",
"01010"]) == 198

def test_problem2():
    assert problem2(["00100",
"11110",
"10110",
"10111",
"10101",
"01111",
"00111",
"11100",
"10000",
"11001",
"00010",
"01010"]) == 230

#  def test_problem2():
    #  assert problem2([199,200,208,210,200,207,240,269,260,263]) == 5
