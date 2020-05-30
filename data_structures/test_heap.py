from .heap import Heap

def test_heap():
    min_heap = Heap(lambda parent, child: parent < child)
    max_heap = Heap(lambda parent, child: parent > child)
    arr = [6, 1, 4, 5, 7, 3, 2, 8, 9]
    min_heap.make_heap(arr)
    max_heap.make_heap(arr)

    assert min_heap.top() == 1
    assert max_heap.top() == 9

    min_heap.pop()
    max_heap.pop()
    assert min_heap.top() == 2
    assert max_heap.top() == 8

    min_heap.pop()
    min_heap.pop()
    max_heap.pop()
    max_heap.pop()

    assert min_heap.top() == 4
    assert max_heap.top() == 6

    min_heap.pop()
    min_heap.pop()
    min_heap.pop()
    min_heap.pop()
    min_heap.pop()
    min_heap.pop()
    assert min_heap.top() is None

    max_heap.pop()
    max_heap.pop()
    max_heap.pop()
    max_heap.pop()
    max_heap.pop()
    max_heap.pop()
    assert max_heap.top() is None
