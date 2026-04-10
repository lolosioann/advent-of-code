def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    # read first line for length and "S" index
    start_idx = list(lines[0].strip()).index("S")

    # recursively add ray split points in the visited list
    visited = []
    count_splits(lines, 1, start_idx, visited)
    print(len(visited))


def count_splits(lines, line_idx, ray_idx, visited):
    if line_idx == len(lines) - 1:
        return
    elif list(lines[line_idx].strip())[ray_idx] != "^":
        count_splits(lines, line_idx + 1, ray_idx, visited)
    else:
        if (line_idx, ray_idx) in visited:
            return
        visited.append((line_idx, ray_idx))
        count_splits(lines, line_idx + 1, ray_idx - 1, visited)
        count_splits(lines, line_idx + 1, ray_idx + 1, visited)


if __name__ == "__main__":
    main()
