def main() -> None:
    total_sum = 0

    with open("input.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        digits = [int(c) for c in line]
        n = len(digits)

        # Each entry: (digit_value, original_index)
        max_vals = [None] * 12
        start = 0

        for i in range(12):
            # limit ensures enough digits remain
            end = n - (12 - i) + 1

            value, idx = argmax(digits[start:end])
            max_vals[i] = (value, start + idx)

            start = start + idx + 1

        number = int("".join(str(max_vals[i][0]) for i in range(12)))
        total_sum += number

    print(total_sum)


def argmax(lst):
    i = max(range(len(lst)), key=lambda k: (lst[k], -k))
    return lst[i], i


if __name__ == "__main__":
    main()
