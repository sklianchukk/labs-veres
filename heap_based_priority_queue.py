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
        if len(self.queue) > 1:
            for i in range((len(self.queue) - 2) // 2, -1, -1):
                self.heapify(self.queue, i, len(self.queue))

    def heapify(self, arr, node, heap_len):
        left_child = node * 2 + 1
        right_child = node * 2 + 2

        if left_child < heap_len:
            if arr[left_child].priority > arr[node].priority:
                self.swap(arr, left_child, node)
                self.heapify(arr, left_child, heap_len)
        if right_child < heap_len:
            if arr[right_child].priority > arr[node].priority:
                self.swap(arr, right_child, node)
                self.heapify(arr, right_child, heap_len)

    def delete(self):
        if len(self.queue) == 0:
            return None
        elif len(self.queue) == 1:
            return self.queue.pop()
        else:
            max_num = self.queue[0]
            self.queue[0] = self.queue.pop()
            for i in range(0, (len(self.queue) - 2) // 2):
                self.heapify(self.queue, i, len(self.queue))
            return max_num.priority

    def peek(self):
        if self.queue:
            return self.queue[0].value
        else:
            return None
