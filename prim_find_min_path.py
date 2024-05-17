import csv

"""
Не повністю правильно працювала моя черга з heap_based_priority_queue.py, тому був змушений її трошки змінити, 
і через те, що 4 лабка вже замерджена, я тут прямо написав відредагові класи з 4 лабки. Все працює тепер правильно
"""


class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class HeapQueue:
    def __init__(self):
        self.queue = []

    def swap(self, arr, a, b):
        arr[a], arr[b] = arr[b], arr[a]

    def insert(self, value, priority):
        new_node = Node(value, priority)
        self.queue.append(new_node)
        index = len(self.queue) - 1
        parent_index = (index - 1) // 2

        while (
            index > 0 and self.queue[parent_index].priority > self.queue[index].priority
        ):
            self.swap(self.queue, parent_index, index)
            index = parent_index
            parent_index = (index - 1) // 2

    def heapify(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        if (
            left_child < len(self.queue)
            and self.queue[left_child].priority < self.queue[smallest].priority
        ):
            smallest = left_child
        if (
            right_child < len(self.queue)
            and self.queue[right_child].priority < self.queue[smallest].priority
        ):
            smallest = right_child
        if smallest != index:
            self.swap(self.queue, index, smallest)
            self.heapify(smallest)

    def delete(self):
        if len(self.queue) == 0:
            return None
        elif len(self.queue) == 1:
            return self.queue.pop()
        else:
            min_element = self.queue[0]
            self.queue[0] = self.queue.pop()
            if len(self.queue) > 0:
                self.heapify(0)
            return min_element

    def peek(self):
        if self.queue:
            return self.queue[0].value
        else:
            return None


def read_matrix_from_csv(file_path):
    matrix = []
    with open(file_path, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            matrix.append([int(weight) if weight.isdigit() else 0 for weight in row])
    return matrix


def create_graph_from_matrix(matrix):
    """
    Function to create a graph using an adjacency matrix.
    Args:
        matrix (list of lists): 2D list representing the adjacency matrix where matrix[i][j] is the weight of the edge between vertices i and j.
    Returns:
        list: Adjacency list for each vertex.
    """
    num_nodes = len(matrix)
    input_graph = [[] for _ in range(num_nodes)]
    for i in range(num_nodes):
        for j in range(num_nodes):
            if matrix[i][j] != 0:  # Assuming 0 means no edge
                input_graph[i].append((j, matrix[i][j]))
    return input_graph


def prim_find_min_path(matrix):
    """
    Implementation of Prim's algorithm for finding MST using a modified Heap from lab_4.

    Args:
        matrix (list of lists): Adjacency matrix representing the graph.
    Returns:
        Length of MST or message about disconnected graph
    """
    amount_of_vertices = len(matrix)
    if amount_of_vertices == 0:
        return "Graph has no vertices"

    prima_graph = create_graph_from_matrix(matrix)
    priority_queue = HeapQueue()
    visited = set()
    visited.add(0)
    length = 0

    for next_vertex, weight in prima_graph[0]:
        priority_queue.insert((0, next_vertex), weight)

    while len(priority_queue.queue) > 0:
        min_edge = priority_queue.delete()
        start_vertex, next_vertex = min_edge.value
        weight = min_edge.priority

        if next_vertex not in visited:
            visited.add(next_vertex)
            length += weight
            for neighbour, distance in prima_graph[next_vertex]:
                if neighbour not in visited:
                    priority_queue.insert((next_vertex, neighbour), distance)

    if len(visited) == amount_of_vertices:
        return length
    else:
        return "Not all vertices are connected, check your graph"
