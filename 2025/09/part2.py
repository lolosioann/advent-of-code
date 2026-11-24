def main():
    points = read_points("input.txt")
    x_ranks, y_ranks = compress_coordinates(points)

    grid = draw_edges(points, x_ranks, y_ranks)
    flood_fill_outside(grid)
    prefix = prefix_sum_of_outside(grid)

    best = 0
    for i, p1 in enumerate(points):
        for p2 in points[i + 1 :]:
            if outside_in_rect(p1, p2, x_ranks, y_ranks, prefix) == 0:
                best = max(best, area(p1, p2))
    print(best)


def read_points(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return [tuple(map(int, line.strip().split(","))) for line in lines]


def area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)


def compress_coordinates(points):
    xs = sorted({p[0] for p in points})
    ys = sorted({p[1] for p in points})
    x_ranks = {x: i + 1 for i, x in enumerate(xs)}
    y_ranks = {y: i + 1 for i, y in enumerate(ys)}
    return x_ranks, y_ranks


def draw_edges(points, x_ranks, y_ranks):
    # 1-cell rim of padding so the outside stays connected
    width = len(x_ranks) + 2
    height = len(y_ranks) + 2
    grid = [[0] * width for _ in range(height)]

    for a, b in zip(points, points[1:] + points[:1]):
        cx1, cy1 = x_ranks[a[0]], y_ranks[a[1]]
        cx2, cy2 = x_ranks[b[0]], y_ranks[b[1]]
        if cx1 == cx2:  # vertical edge
            for cy in range(min(cy1, cy2), max(cy1, cy2) + 1):
                grid[cy][cx1] = 1
        else:  # horizontal edge
            for cx in range(min(cx1, cx2), max(cx1, cx2) + 1):
                grid[cy1][cx] = 1

    return grid


def flood_fill_outside(grid):
    height = len(grid)
    width = len(grid[0])

    stack = [(0, 0)]
    grid[0][0] = 2  # outside

    while stack:
        cx, cy = stack.pop()
        for nx, ny in ((cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)):
            if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] == 0:
                grid[ny][nx] = 2
                stack.append((nx, ny))


def prefix_sum_of_outside(grid):
    height = len(grid)
    width = len(grid[0])
    # pref[cy][cx] = outside cells strictly above and to the left of (cx, cy)
    pref = [[0] * (width + 1) for _ in range(height + 1)]

    for cy in range(height):
        for cx in range(width):
            pref[cy + 1][cx + 1] = (
                (1 if grid[cy][cx] == 2 else 0)
                + pref[cy][cx + 1]
                + pref[cy + 1][cx]
                - pref[cy][cx]
            )
    return pref


def outside_in_rect(p1, p2, x_ranks, y_ranks, pref):
    cx1, cx2 = sorted((x_ranks[p1[0]], x_ranks[p2[0]]))
    cy1, cy2 = sorted((y_ranks[p1[1]], y_ranks[p2[1]]))
    return (
        pref[cy2 + 1][cx2 + 1]
        - pref[cy1][cx2 + 1]
        - pref[cy2 + 1][cx1]
        + pref[cy1][cx1]
    )


if __name__ == "__main__":
    main()
