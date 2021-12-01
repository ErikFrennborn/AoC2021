import importlib

CURRENT_DAY = 1

def getInput(day):
    data_raw = []
    with open(f"inputs/{day}") as inputfile:
        data_raw = inputfile.readlines()

    data_as_number = list(map(int, data_raw))
    return (data_raw, data_as_number)

def main():
    for i in range(CURRENT_DAY):
        i =+1
        today_code = importlib.import_module(f"day{i}")
        (data_raw, data_as_number) = getInput(i)
        print(f"Day {i}:")
        today_code.main(data_raw,data_as_number)


if __name__ == "__main__":
    main()
