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
    valid_ingredients = []
    for ingredient in ingredients:
        if any(start <= ingredient <= end for start, end in ranges):
            valid_ingredients.append(ingredient)
    return valid_ingredients


if __name__ == "__main__":
    main()
