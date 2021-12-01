import importlib
import sys

CURRENT_DAY = 1

def getInput(day):
    data_raw = []
    with open(f"inputs/{day}") as inputfile:
        data_raw = inputfile.readlines()

    data_as_number = list(map(int, data_raw))
    return (data_raw, data_as_number)

def main(argv):
    match argv:
        case ["-t", day, file]:
            data_raw = []
            with open(f"test_data/{file}") as inputfile:
                data_raw = inputfile.readlines()

            data_as_number = list(map(int, data_raw))

            code = importlib.import_module(f"src.day{day}")
            code.main(data_raw,data_as_number)
        case _:
            for i in range(CURRENT_DAY):
                i =+1
                code = importlib.import_module(f"src.day{i}")
                (data_raw, data_as_number) = getInput(i)
                print(f"Day {i}:")
                code.main(data_raw,data_as_number)


if __name__ == "__main__":
    main(sys.argv[1:])
