def depth_first_search(network, source, target):

    seen = set()
    nodes = [source]

    while len(nodes) > 0:

        current = nodes.pop()

        if current not in seen:

            print("Node reached:", current)
            seen.add(current)

            if current == target:
                print("Target node found!")
                return

            children = network.get(current, [])

            for item in reversed(children):
                nodes.append(item)


graph_data = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

depth_first_search(graph_data, 'A', 'F')