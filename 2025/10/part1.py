from functools import reduce
from itertools import combinations
from operator import xor


def to_bin(pattern: str) -> int:
    bits = 0
    for i, char in enumerate(pattern.strip("[]")):
        if char == "#":
            bits |= 1 << i
    return bits


def to_bin_list(wirings: list[str]) -> list[int]:
    masks = []
    for wiring in wirings:
        mask = 0
        for entry in wiring.strip("()").split(","):
            mask ^= 1 << int(entry)
        masks.append(mask)
    return masks


def min_presses(target: int, buttons: list[int]) -> int:
    """Pressing a button twice is a no-op, so the minimum is over subsets."""
    for count in range(len(buttons) + 1):
        for combo in combinations(buttons, count):
            if reduce(xor, combo, 0) == target:
                return count
    raise ValueError("target unreachable")


def main() -> None:
    total = 0
    with open("input.txt") as f:
        for line in f:
            parts = line.split()
            target = to_bin(parts[0])
            buttons = to_bin_list(parts[1:-1])  # last token is the {joltages}
            total += min_presses(target, buttons)
    print(total)


if __name__ == "__main__":
    main()
