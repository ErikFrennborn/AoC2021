from functools import total_ordering


def createGraph(data):
    graph = {}
    unique_points = set([item for sublist in data for item in sublist])
    for point in unique_points:
        graph[point] = set()

    # Populate connection
    for line in data:
        graph[line[0]].add(line[1])
        graph[line[1]].add(line[0])

    return graph

def exploreCave(graph, have_explored, current, expection):
    paths = []
    have_explored[current] += 1

    # base case
    if current == "end":
        return [["end"]]

    for next_caves in graph[current]:
        # Don't got back to small caves
        limit = 2 if next_caves == expection else 1
        if next_caves.islower() and have_explored[next_caves] == limit:
            continue

        # We should go back to start
        if next_caves == "start":
            continue

        # Recursively search valid connected caves
        for result in exploreCave(graph, have_explored.copy(), next_caves, expection):
            result.append(current)
            paths.append(result)

    return paths

def problem1(data):
    graph = createGraph(data)

    unique_points = set([item for sublist in data for item in sublist])
    has_explored = {}
    for point in unique_points:
        has_explored[point] = 0


    # Recursively explore graph
    return len(exploreCave(graph, has_explored, "start",None))

def problem2(data):
    graph = createGraph(data)
    unique_points = set([item for sublist in data for item in sublist])
    has_explored = {}
    for point in unique_points:
        has_explored[point] = 0


    total_paths = set()
    for point in unique_points:
        if point == "start" or point == "end":
            continue
        total_paths = total_paths.union(set(list(map(lambda x:''.join(x),exploreCave(graph, has_explored.copy(), "start", point)))))
    return len(total_paths)



def main(data,_):
    parsedInput = list(map(lambda x: x.strip().split('-'), data))
    print(f"Problem 1: {problem1(parsedInput)}")
    print(f"Problem 2: {problem2(parsedInput)}")

def test_problem1_a():
    data = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc""".split('\n')
    parsedInput = list(map(lambda x: x.strip().split('-'), data))
    assert problem1(parsedInput) == 19

def test_problem1_b():
    data = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW""".split('\n')
    parsedInput = list(map(lambda x: x.strip().split('-'), data))
    assert problem1(parsedInput) == 226



def test_problem2_a():
    data="""start-A
start-b
A-c
A-b
b-d
A-end
b-end""".split('\n')
    parsedInput = list(map(lambda x: x.strip().split('-'), data))
    assert problem2(parsedInput) == 36

def test_problem2_b():
    data = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc""".split('\n')
    parsedInput = list(map(lambda x: x.strip().split('-'), data))
    assert problem2(parsedInput) == 103

def test_problem2_c():
    data = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW""".split('\n')
    parsedInput = list(map(lambda x: x.strip().split('-'), data))
    assert problem2(parsedInput) == 3509

