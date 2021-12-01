import importlib
import sys
from datetime import datetime
import os


YEAR = 2021

CURRENT_DAY = (datetime.now() - datetime.strptime(f"{YEAR}-11-30","%Y-%m-%d") ).days

def getInput(day):
    data_raw = []
    with open(f"inputs/{day}") as inputfile:
        data_raw = inputfile.readlines()

    data_as_number = list(map(int, data_raw))
    return (data_raw, data_as_number)

def fetch(day):
    print(os.system(f'curl --cookie "session={os.environ["AOC_TOKEN"]}" https://adventofcode.com/{YEAR}/day/{day}/input > inputs/{day}'))

def run(day):
    code = importlib.import_module(f"src.day{day}")
    (data_raw, data_as_number) = getInput(day)
    print(f"Day {day}:")
    code.main(data_raw,data_as_number)


def main(argv):
    match argv:
        case ["-f", day]:
            fetch(day)
        case ["-f"]:
            for i in range(CURRENT_DAY):
                i += 1
                fetch(i)

        case ["-t", day, file]:
            data_raw = []
            with open(f"test_data/{file}") as inputfile:
                data_raw = inputfile.readlines()

            data_as_number = list(map(int, data_raw))

            code = importlib.import_module(f"src.day{day}")
            code.main(data_raw,data_as_number)
        case ["-r", day]:
            run(day)
        case ["-r"]:
            for i in range(CURRENT_DAY):
                i =+1
                run(i)

if __name__ == "__main__":
    main(sys.argv[1:])
