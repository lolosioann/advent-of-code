def main():
    ranges = parse_input("input.txt")
    merged_ranges = merge_ranges(ranges)
    count = sum(end - start + 1 for start, end in merged_ranges)
    print(count)


def parse_input(filename):
    ranges = []

    with open(filename, "r") as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if line == "":
            break
        parts = line.split("-")
        ranges.append((int(parts[0]), int(parts[1])))
    return ranges


def merge_ranges(ranges):
    ranges.sort(key=lambda x: x[0])
    merged = []
    current_start, current_end = ranges[0]
    for start, end in ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end
    merged.append((current_start, current_end))
    return merged


if __name__ == "__main__":
    main()
