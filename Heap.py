class MinHeap:
    def __init__ (self):
        self.heap = [0]
        self.size= 0

    def insert(self, data):
            self.heap.append(data)
            self.size += 1
            self._arrange(self.size)

    def delete_at_root(self):
            if self.size == 0:
                return None
            
            root_value = self.heap[1]
            self.heap[1] = self.heap[self.size]
            self.heap.pop()
            self.size -= 1
            
            if self.size > 0:
                self._sink(1)
                
            return root_value

    def delete_at_location(self, location):
            if location < 1 or location > self.size:
                print(f"Error: Ubicación {location} fuera de rango.")
                return None
            
            deleted_value = self.heap[location]
            last_value = self.heap[self.size]

            self.heap[location] = last_value
            self.heap.pop()
            self.size -= 1
            if location <= self.size:
                self._sink(location)
                if location <= self.size and self.heap[location] == last_value:
                    self._arrange(location)
                    
            return deleted_value

    def heap_sort(self):
            sorted_list = []
            while self.size > 0:
                sorted_list.append(self.delete_at_root())
            return sorted_list
        
        
        
        
    def _arrange(self, i):
            while i // 2 > 0:

                if self.heap[i] < self.heap[i // 2]:
                    self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
                i = i // 2

    def _sink(self, i):
            while (i * 2) <= self.size:
                mc = self._min_child(i)
                if self.heap[i] > self.heap[mc]:
                    self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
                i = mc

    def _min_child(self, i):
            if (i * 2) + 1 > self.size:
                return i * 2
            else:
                if self.heap[i * 2] < self.heap[(i * 2) + 1]:
                    return i * 2
                else:
                    return (i * 2) + 1

    def __str__(self):

            return str(self.heap[1:])

if __name__ == "__main__":
    print("MiniHeap creo")
    mi_heap = MinHeap()
    elementos = [15, 5, 20, 1, 12, 3]
    print(f"Insertando elementos: {elementos}")
    for el in elementos:
        mi_heap.insert(el)
    print(f"Heap actual: {mi_heap}")
    print("Eliminando en la Raíz")
    minimo = mi_heap.delete_at_root()
    print(f"Elemento eliminado (Raíz): {minimo}")
    print(f"Heap tras eliminar la raíz: {mi_heap}")

    print("Eliminando en una ubicación específica")
    posicion = 2
    eliminado = mi_heap.delete_at_location(posicion)
    print(f"Elemento eliminado en la posición {posicion}: {eliminado}")
    print(f"Heap tras la eliminación: {mi_heap}")

    print("Ejecución del Heap Sort ")
    lista_ordenada = mi_heap.heap_sort()
    print(f"Lista completamente ordenada: {lista_ordenada}")
    print(f"Heap final : {mi_heap}")
