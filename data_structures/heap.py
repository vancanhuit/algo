class Heap:
    def __init__(self, comparator):
        self._elems = []
        self._comparator = comparator

    def top(self):
        if len(self._elems) == 0:
            return None
        return self._elems[0]

    def push(self, value):
        self._elems.append(value)
        self._heapify_up(len(self._elems) - 1)

    def pop(self):
        if len(self._elems) == 0:
            return
        if len(self._elems) == 1:
            self._elems.pop()
            return
        self._elems[0] = self._elems.pop()
        self._heapify_down(0)

    def make_heap(self, arr):
        for _, v in enumerate(arr):
            self._elems.append(v)

        index = (len(self._elems) - 1) // 2
        for i in range(index, - 1, -1):
            self._heapify_down(i)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if parent == -1:
            return
        if not self._comparator(self._elems[parent], self._elems[index]):
            self._elems[parent], self._elems[index] = \
                 self._elems[index], self._elems[parent]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        if index >= len(self._elems):
            return
        left = 2 * index + 1
        right = 2 * index + 2
        i = index
        if left < len(self._elems) and \
             not self._comparator(self._elems[i], self._elems[left]):
            i = left
        if right < len(self._elems) and \
             not self._comparator(self._elems[i], self._elems[right]):
            i = right

        if i != index:
            self._elems[index], self._elems[i] = \
                 self._elems[i], self._elems[index]
            self._heapify_down(i)
