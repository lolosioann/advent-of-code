def main():
    pos = 50
    times_past_zero_total = 0

    with open("input.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        direction, amount = get_pos_amount(line)
        pos, times_past_zero = move_pos(pos, direction, amount)
        times_past_zero_total += times_past_zero
        pos %= 100  # wrap position around 100
    print(f"Times past zero: {times_past_zero_total}")


def get_pos_amount(line):
    line = line.strip()
    direction, amount = line[0], int(line[1:])
    return direction, amount


def move_pos(pos, direction, amount):
    start = pos
    times_past_zero = 0
    match direction:
        case "R":
            pos += amount
        case "L":
            pos -= amount
            if pos < 0 and start != 0:
                times_past_zero += 1
        case _:
            raise ValueError(f"Unknown direction: {direction}")

    times_past_zero += abs(pos) // 100
    if pos == 0:
        times_past_zero += 1
    return pos, times_past_zero


if __name__ == "__main__":
    main()
