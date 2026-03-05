def depth_limited(current, target, limit):

    if current == target:
        return True

    if limit == 0:
        return False

    neighbours = tree.get(current, [])

    for nxt in neighbours:
        result = depth_limited(nxt, target, limit - 1)
        if result:
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

answer = depth_limited('A', 'F', 2)

print("Goal reachable within depth limit:", answer)