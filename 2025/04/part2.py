from itertools import product


def main():
    mat = read_as_matrix("input.txt", str)
    mat = add_padding(mat, pad_value=".")

    total_accessible_rolls = 0

    while True:
        newly_accessible = calc_accessible_rolls(mat)

        if newly_accessible == 0:
            break

        total_accessible_rolls += newly_accessible

    print(total_accessible_rolls)


def read_as_matrix(file_path, element_type=int):
    with open(file_path, "r") as file:
        return [list(map(element_type, line.strip())) for line in file.readlines()]


def add_padding(matrix, pad_value=0):
    if not matrix:
        return []

    cols = len(matrix[0])
    padded_row = [pad_value] * (cols + 2)

    return (
        [padded_row] + [[pad_value, *row, pad_value] for row in matrix] + [padded_row]
    )


def calc_accessible_rolls(matrix, target_value="@", bad_value="@", empty_value="."):
    rows = len(matrix)
    cols = len(matrix[0]) if rows else 0

    neighbor_offsets = [
        (dr, dc)
        for dr, dc in product([-1, 0, 1], repeat=2)
        if not (dr == 0 and dc == 0)
    ]

    accessible_rolls = 0

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if matrix[r][c] != target_value:
                continue

            bad_neighbors = sum(
                matrix[r + dr][c + dc] == bad_value for dr, dc in neighbor_offsets
            )

            if bad_neighbors < 4:
                accessible_rolls += 1
                matrix[r][c] = empty_value  # replace with empty

    return accessible_rolls


if __name__ == "__main__":
    main()
