class Node:
    def __init__(self, name: str):
        self.name = name
        self.children = []


def find_all_paths(graph, src, dst, path=None):
    if not path:
        path = []

    path = path + [src]

    if src == dst:
        return [path]

    paths = []
    for node in graph[src].children:
        if node in path:
            continue  # avoids cycles
        new_paths = find_all_paths(graph, node, dst, path)
        paths.extend(new_paths)

    return paths


def main():
    nodes = {}
    with open("input.txt", "r") as f:
        for line in f:
            data = line.split(" ")
            data[0] = data[0].strip(":")
            data[-1] = data[-1].strip("\n")
            nodes[data[0]] = Node(data[0])
            for node in data[1:]:
                if node not in nodes:
                    nodes[node] = Node(node)
                nodes[data[0]].children.append(node)

    print(len(find_all_paths(nodes, "you", "out")))


if __name__ == "__main__":
    main()
