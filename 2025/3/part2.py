from typing import List, Optional, Tuple


def main() -> None:
    total_sum: int = 0

    with open("input.txt", "r") as file:
        lines: List[str] = file.readlines()

    for line in lines:
        line = line.strip()
        digits: List[int] = [int(c) for c in line]
        n: int = len(digits)

        # Each entry: (digit_value, original_index)
        max_vals: List[Optional[Tuple[int, int]]] = [None] * 12
        start: int = 0  # sliding start index

        for i in range(12):
            # limit ensures enough digits remain
            end: int = n - (12 - i) + 1

            value, idx = argmax(digits[start:end])
            max_vals[i] = (value, start + idx)

            start = start + idx + 1

        number: int = int("".join(str(max_vals[i][0]) for i in range(12)))
        total_sum += number

    print(total_sum)


def argmax(lst: List[int]) -> Tuple[int, int]:
    i: int = max(range(len(lst)), key=lambda k: (lst[k], -k))
    return lst[i], i


if __name__ == "__main__":
    main()
