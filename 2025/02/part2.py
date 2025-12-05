def main():
    total_sum = 0
    with open("input.txt", "r") as file:
        lines = file.readlines()

    id_ranges = lines[0].strip().split(",")

    for id_range in id_ranges:
        start, end = map(int, id_range.split("-"))
        for i in range(start, end + 1):
            if check_invalid(i):
                total_sum += i

    print(f"Sum of invalid IDs: {total_sum}")


def check_invalid(id_number):
    s = str(id_number)
    n = len(s)

    for k in range(1, n // 2 + 1):
        if n % k == 0:
            pattern = s[:k]
            if pattern * (n // k) == s:
                return True

    return False


if __name__ == "__main__":
    main()
