import csv
import heapq

def read_graph(filename):
    """
    Reads a graph from a CSV file and returns it as an adjacency matrix.
    :return: The graph represented as an adjacency matrix.
    """
    matrix = []
    with open(filename, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            processed_row = [float(val) if val != "None" else None for val in row]
            matrix.append(processed_row)
    return matrix


def add_edges(source_vertex, matrix, visited, min_heap):
    """
    Adds edges from a given vertex to the min heap.
    """
    visited[source_vertex] = True
    for i in range(len(matrix)):
        if matrix[source_vertex][i] is not None and not visited[i]:
            heapq.heappush(min_heap, (matrix[source_vertex][i], i))

def prim_find_min_path(matrix, start_vertex=0):
    """
    Finds the minimum spanning tree using Prim's algorithm optimized with a min-heap.
    :return: The weight of the minimum spanning tree.
    """
    n = len(matrix)
    visited = [False] * n
    min_heap = []
    total_weight = 0

    add_edges(start_vertex, matrix, visited, min_heap)

    while min_heap:
        weight, next_vertex = heapq.heappop(min_heap)
        if not visited[next_vertex]:
            total_weight += weight
            add_edges(next_vertex, matrix, visited, min_heap)

    return total_weight

imported_graph = read_graph("islands.csv")

mst_weight = prim_find_min_path(imported_graph)
print("Total weight of the minimum spanning tree:", int(mst_weight))
