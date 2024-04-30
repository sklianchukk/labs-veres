from collections import deque


def read_from_input(file_path):
    graph = {}
    with open(file_path, "r") as file:
        root = file.readline().strip()
        for line in file:
            node1, node2 = line.strip().split(",")
            if node1 not in graph:
                graph[node1] = []
            graph[node1].append(node2)
            if node2 not in graph:
                graph[node2] = []
    return graph, root


def find_min_length(graph, start_node):
    queue = deque([(start_node, 0)])

    while queue:
        current_node, depth = queue.popleft()

        if not graph[current_node]:
            return depth + 1

        for children in graph[current_node]:
            queue.append((children, depth + 1))


def write_to_output(length, file_path):
    with open(file_path, "w") as file:
        file.write(str(length))


input_file = "input.txt"
graph, root = read_from_input(input_file)

length = find_min_length(graph, root)

output_file = "output.txt"
write_to_output(length, output_file)
