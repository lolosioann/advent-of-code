from z3 import Int, Optimize, Sum, sat


def min_presses(target: list[int], buttons: list[tuple[int, ...]]) -> int:
    presses = [Int(f"p{i}") for i in range(len(buttons))]
    opt = Optimize()
    for p in presses:
        opt.add(p >= 0)
    for j, value in enumerate(target):
        opt.add(Sum(presses[i] for i, b in enumerate(buttons) if j in b) == value)
    opt.minimize(Sum(presses))
    assert opt.check() == sat
    return opt.model().evaluate(Sum(presses)).as_long()


def main() -> None:
    total = 0
    with open("input.txt") as f:
        for line in f:
            parts = line.split()
            target = list(map(int, parts[-1].strip("{}").split(",")))
            buttons = [
                tuple(map(int, part.strip("()").split(","))) for part in parts[1:-1]
            ]
            total += min_presses(target, buttons)
    print(total)


if __name__ == "__main__":
    main()
