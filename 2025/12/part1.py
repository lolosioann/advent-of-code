import re


def orientations(cells: set[tuple[int, int]]) -> set[frozenset[tuple[int, int]]]:
    out: set[frozenset[tuple[int, int]]] = set()
    for a, b, c, d in [
        (1, 0, 0, 1), (0, -1, 1, 0), (-1, 0, 0, -1), (0, 1, -1, 0),
        (1, 0, 0, -1), (-1, 0, 0, 1), (0, 1, 1, 0), (0, -1, -1, 0),
    ]:
        transformed = {(a * x + b * y, c * x + d * y) for x, y in cells}
        min_x = min(x for x, _ in transformed)
        min_y = min(y for _, y in transformed)
        out.add(frozenset((x - min_x, y - min_y) for x, y in transformed))
    return out


def can_pack(w: int, h: int, counts: list[int], variants: list[list[frozenset]]) -> bool:
    # 0 = empty, 1 = present, 2 = permanent hole (region cells need not all be filled)
    grid = [[0] * w for _ in range(h)]
    areas = [len(v[0]) for v in variants]
    remaining = sum(counts[i] * areas[i] for i in range(len(counts)))
    occupied = 0
    blocked = 0

    def first_empty() -> tuple[int, int] | None:
        for y in range(h):
            for x in range(w):
                if grid[y][x] == 0:
                    return x, y
        return None

    def fits(ax: int, ay: int, cells: frozenset) -> bool:
        return all(
            0 <= ax + ox < w and 0 <= ay + oy < h and grid[ay + oy][ax + ox] == 0
            for ox, oy in cells
        )

    def search() -> bool:
        nonlocal occupied, blocked, remaining
        if remaining == 0:
            return True
        if remaining > w * h - occupied - blocked:
            return False
        pos = first_empty()
        if pos is None:
            return False
        fx, fy = pos
        for i in range(len(counts)):
            if counts[i] == 0:
                continue
            for cells in variants[i]:
                for ox, oy in cells:
                    ax, ay = fx - ox, fy - oy
                    if fits(ax, ay, cells):
                        for px, py in cells:
                            grid[ay + py][ax + px] = 1
                        counts[i] -= 1
                        occupied += areas[i]
                        remaining -= areas[i]
                        if search():
                            return True
                        remaining += areas[i]
                        occupied -= areas[i]
                        counts[i] += 1
                        for px, py in cells:
                            grid[ay + py][ax + px] = 0
        grid[fy][fx] = 2
        blocked += 1
        if search():
            return True
        blocked -= 1
        grid[fy][fx] = 0
        return False

    return search()


def solve(text: str) -> int:
    lines = text.splitlines()
    split = next(i for i, line in enumerate(lines) if re.match(r"\d+x\d+:", line.strip()))

    blocks: list[list[str]] = []
    current: list[str] = []
    for line in lines[:split]:
        if not line.strip():
            if current:
                blocks.append(current)
                current = []
        else:
            current.append(line.strip())
    if current:
        blocks.append(current)

    shapes: dict[int, set[frozenset]] = {}
    for block in blocks:
        sid = int(block[0].rstrip(":"))
        cells = {
            (x, y)
            for y, row in enumerate(block[1:])
            for x, ch in enumerate(row)
            if ch == "#"
        }
        shapes[sid] = orientations(cells)

    total = 0
    for line in lines[split:]:
        line = line.strip()
        if not line:
            continue
        size, rest = line.split(":", 1)
        w, h = map(int, size.split("x"))
        counts = list(map(int, rest.split()))

        if (w // 3) * (h // 3) >= sum(counts):
            total += 1
            continue

        if sum(counts[i] * len(next(iter(shapes[i]))) for i in range(len(counts))) > w * h:
            continue

        if can_pack(w, h, counts, [list(shapes[i]) for i in range(len(counts))]):
            total += 1

    return total


def main() -> None:
    with open("input.txt") as f:
        print(solve(f.read()))


if __name__ == "__main__":
    main()
