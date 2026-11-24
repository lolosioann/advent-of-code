from functools import cache


def parse_graph(lines: list[str]) -> dict[str, list[str]]:
    graph: dict[str, list[str]] = {}
    for line in lines:
        src, *children = line.split()
        graph[src.strip(":")] = children
        for child in children:
            graph.setdefault(child, [])
    return graph


def path_counter(graph: dict[str, list[str]]):
    @cache
    def count(src: str, dst: str) -> int:
        if src == dst:
            return 1
        return sum(count(child, dst) for child in graph[src])

    return count


def main() -> None:
    with open("input.txt") as f:
        graph = parse_graph(f.readlines())
    count = path_counter(graph)
    via_dac_first = count("svr", "dac") * count("dac", "fft") * count("fft", "out")
    via_fft_first = count("svr", "fft") * count("fft", "dac") * count("dac", "out")
    print(via_dac_first + via_fft_first)


if __name__ == "__main__":
    main()
