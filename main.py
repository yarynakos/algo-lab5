from models.node import Node


def count_levels(node) -> int:
    parent_node = node.parent
    count = 1
    while parent_node is not None:
        count += 1
        parent_node = parent_node.parent
    return count


def find_min_depth(root):
    queue = [root]
    arr_of_ends = []
    arr_of_counts = []
    while len(queue) > 0:
        if queue[0].left_child is None and queue[0].right_child is None:
            arr_of_ends.append(queue[0])
        else:
            if queue[0].left_child is not None:
                queue.append(queue[0].left_child)
            if queue[0].right_child is not None:
                queue.append(queue[0].right_child)
        del queue[0]
    while len(arr_of_ends) > 0:
        arr_of_counts.append(count_levels(arr_of_ends[0]))
        del arr_of_ends[0]
    min_depth = arr_of_counts[0]
    for i in range(0, len(arr_of_counts)):
        if min_depth > arr_of_counts[i]:
            min_depth = arr_of_counts[i]
    with open('output.txt', 'w') as file:
        file.write(str(min_depth))


if __name__ == '__main__':
    graph = {}
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        root = int(lines[0].strip())
        graph[root] = Node(root, None, None, None)
        for line in lines[1:]:
            parent, node = map(int, line.strip().split(','))
            if node not in graph:
                graph[node] = Node(node, graph[parent], None, None)
            if graph[parent].left_child is None:
                graph[parent].left_child = graph[node]
            else:
                graph[parent].right_child = graph[node]
    find_min_depth(graph[1])
