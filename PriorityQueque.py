def main(Node):
    pq = PriorityQueueHeap()

    pq.enqueue("perro", 1)
    pq.enqueue("gato", 3)
    pq.enqueue("pez", 2)
    pq.enqueue("conejo", 5)
    pq.enqueue("hamster", 4)

    sorted = pq.heap_sort()
    for e in sorted:
        print(e)


class Node:
    def __init__(self, value, priority):
        self.priority = priority
        self.value = value

    def __str__(self):
        return f"({self.value}, {self.priority})"
   
class PriorityQueueHeap:

    def __init__(self):
        self.heap = []

    def enqueue(self, value, priority):
        node = Node(value, priority)
        self.heap.append(node)
        self.arrange(len(self.heap) - 1)

    def arrange(self, location):
        while location > 0:
            parent = (location - 1) // 2

            if self.heap[parent].priority > self.heap[location].priority:
                self.heap[parent], self.heap[location] = \
                    self.heap[location], self.heap[parent]

                location = parent
            else:
                break

    def dequeue(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()

        self.sink(0)

        return root

    def sink(self, location):
        while True:
            child = self.minchild(location)

            if child is None:
                break

            if self.heap[location].priority > self.heap[child].priority:
                self.heap[location], self.heap[child] = \
                    self.heap[child], self.heap[location]

                location = child
            else:
                break

    def minchild(self, location):
        left = 2 * location + 1
        right = 2 * location + 2

        if left >= len(self.heap):
            return None

        if right >= len(self.heap):
            return left

        if self.heap[left].priority < self.heap[right].priority:
            return left
        else:
            return right
   
    def heap_sort(self):
       
        sorted_list = []

        while len(self.heap) > 0:
            sorted_list.append(self.dequeue())
       
        return sorted_list

    def __str__(self):
        return str([(node.priority, node.value) for node in self.heap])

main(Node)