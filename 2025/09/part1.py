def area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    data = []
    for line in lines:
        data.append(tuple(map(int, line.strip().split(","))))

    areas = [area(p1, p2) for i, p1 in enumerate(data) for p2 in data[i + 1 :]]
    print(max(areas))


if __name__ == "__main__":
    main()
