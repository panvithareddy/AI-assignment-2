def limited_search(current, target, level):

    if current == target:
        return True

    if level == 0:
        return False

    neighbours = tree.get(current, [])

    for nxt in neighbours:
        if limited_search(nxt, target, level - 1):
            return True

    return False


def iterative_deepening(source, goal, max_limit):

    for depth_level in range(max_limit + 1):

        if limited_search(source, goal, depth_level):
            return True

    return False


tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

result = iterative_deepening('A', 'F', 5)

print("IDDFS Search Result:", result)