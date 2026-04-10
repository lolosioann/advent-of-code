def main():
    total_sum = 0
    with open("input.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        n = len(line)
        digits = [int(char) for char in line]

        max_1, idx = argmax(digits[: n - 1])
        max_2, _ = argmax(digits[idx + 1 :])

        total_sum += max_1 * 10 + max_2

    print(total_sum)


def argmax(lst):
    i = max(range(len(lst)), key=lambda k: (lst[k], -k))
    return lst[i], i


if __name__ == "__main__":
    main()
