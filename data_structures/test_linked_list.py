from .linked_list import SinglyLinkedList, DoublyLinkedList


def test_singly_linked_list():
    l = SinglyLinkedList()
    assert l.is_empty()
    l.insert_first(1)
    l.insert_last(2)
    l.insert_last(3)
    l.insert_first(0)
    assert str(l) == '0->1->2->3'
    l.remove_first()
    assert str(l) == '1->2->3'
    l.remove_last()
    assert str(l) == '1->2'
    l.remove_last()
    assert str(l) == '1'
    l.remove_first()
    assert l.is_empty()
    assert str(l) == ''


def test_doubly_linked_list():
    l = DoublyLinkedList()
    assert l.is_empty()
    l.insert_first(1)
    l.insert_last(2)
    l.insert_last(3)
    l.insert_first(0)
    assert str(l) == '0->1->2->3'
    assert l.reverse() == '3<-2<-1<-0'
    l.remove_first()
    assert str(l) == '1->2->3'
    assert l.reverse() == '3<-2<-1'
    l.remove_last()
    assert str(l) == '1->2'
    assert l.reverse() == '2<-1'
    l.remove_first()
    l.remove_last()
    assert str(l) == ''
    assert l.reverse() == ''
