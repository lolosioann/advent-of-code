from functools import lru_cache


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    # read first line for length and "S" index
    start_idx = list(lines[0].strip()).index("S")

    cnt = count_paths(tuple(lines), 1, start_idx)
    print(cnt)


@lru_cache(maxsize=None)
def count_paths(lines, line_idx, ray_idx):
    if line_idx == len(lines) - 1:
        return 1
    elif list(lines[line_idx].strip())[ray_idx] != "^":
        return count_paths(lines, line_idx + 1, ray_idx)
    else:
        return count_paths(lines, line_idx + 1, ray_idx - 1) + count_paths(
            lines, line_idx + 1, ray_idx + 1
        )


if __name__ == "__main__":
    main()
