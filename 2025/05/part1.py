def main():
    ranges, ingredients = parse_input("input.txt")
    valid_ingredients = filter_valid_ingredients(ingredients, ranges)
    print(f"Number of valid ingredients: {len(valid_ingredients)}")


def parse_input(filename):
    ranges = []
    ingredients = []
    parse_ranges = True

    with open(filename, "r") as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if line == "":
            parse_ranges = False
            continue
        if parse_ranges:
            parts = line.split("-")
            ranges.append((int(parts[0]), int(parts[1])))
        else:
            ingredients.append(int(line))
    return ranges, ingredients


def filter_valid_ingredients(ingredients, ranges):
    return [i for i in ingredients if any(lo <= i <= hi for lo, hi in ranges)]


if __name__ == "__main__":
    main()
