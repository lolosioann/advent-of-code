from enum import Enum


class Operation(Enum):
    ADD = "+"
    MULTIPLY = "*"


def main():
    with open("input.txt", "r") as file:
        data = [list(line.rstrip("\n")) for line in file]

    ops_row = data[-1]
    rows = data[:-1]

    res = 0
    total = 0
    current_op = Operation.ADD.value  # default operation

    for col, char in enumerate(ops_row):
        # Detect operator
        if char in (Operation.ADD.value, Operation.MULTIPLY.value):
            total += res
            res = 0 if char == Operation.ADD.value else 1
            current_op = char

        # Extract vertical number
        col_chars = [row[col] for row in rows]
        num_str = "".join(col_chars).strip()

        if num_str.isdigit():
            num = int(num_str)
            if current_op == Operation.ADD.value:
                res += num
            else:
                res *= num

    print(res + total)


if __name__ == "__main__":
    main()
