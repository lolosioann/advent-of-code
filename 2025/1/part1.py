def main():
    pos = 50
    times_at_zero = 0

    with open("input.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        direction, amount = get_pos_amount(line)
        pos = move_pos(pos, direction, amount)
        pos = wrap_position(pos)
        if pos == 0:
            times_at_zero += 1

    print(f"Times at position 0: {times_at_zero}")


def get_pos_amount(line):
    line = line.strip()
    direction, amount = line[0], int(line[1:])
    return direction, amount


def move_pos(pos, direction, amount):
    match direction:
        case "R":
            pos += amount
        case "L":
            pos -= amount
        case _:
            raise ValueError(f"Unknown direction: {direction}")

    return pos


def wrap_position(pos):
    pos = pos % 100
    return pos


if __name__ == "__main__":
    main()
