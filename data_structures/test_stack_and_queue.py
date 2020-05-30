from .stack_and_queue import Stack, Queue


def test_stack():
    s = Stack()
    assert s.is_empty()
    s.push(1)
    s.push(2)
    s.push(3)

    assert s.top() == 3
    s.pop()
    assert s.top() == 2
    s.pop()
    s.pop()
    assert s.is_empty()
    assert s.top() is None


def test_queue():
    q = Queue()
    assert q.is_empty()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    assert q.peek() == 1
    q.dequeue()
    assert q.peek() == 2
    q.dequeue()
    q.dequeue()
    assert q.is_empty()
    assert q.peek() is None
