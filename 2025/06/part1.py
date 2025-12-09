from enum import Enum


class Operation(Enum):
    ADD = "+"
    MULTIPLY = "*"


def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        ops = lines[-1].strip().split()
        data = [list(map(int, line.split())) for line in lines[:-1] if line.strip()]

    total = 0
    for col, op in enumerate(ops):
        # extract column `col`
        column_values = [row[col] for row in data]

        if op == Operation.ADD.value:
            res = sum(column_values)

        elif op == Operation.MULTIPLY.value:
            res = 1
            for num in column_values:
                res *= num

        total += res
    print(total)


if __name__ == "__main__":
    main()
