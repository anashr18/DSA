import pytest
from remove2 import remove_nth_last_node
from linkedlist import LinkedList, ListNode

def list_to_linkedlist(lst):
    ll = LinkedList()
    ll.create_linked_list(lst)
    return ll.head

def linkedlist_to_list(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

def test_remove_middle():
    head = list_to_linkedlist([1, 2, 3, 4, 5])
    new_head = remove_nth_last_node(head, 2)
    assert linkedlist_to_list(new_head) == [1, 2, 3, 5]

def test_remove_head():
    head = list_to_linkedlist([10, 20, 30])
    new_head = remove_nth_last_node(head, 3)
    assert linkedlist_to_list(new_head) == [20, 30]

def test_remove_tail():
    head = list_to_linkedlist([7, 8, 9])
    new_head = remove_nth_last_node(head, 1)
    assert linkedlist_to_list(new_head) == [7, 8]

def test_remove_only_element():
    head = list_to_linkedlist([42])
    new_head = remove_nth_last_node(head, 1)
    assert linkedlist_to_list(new_head) == []

def test_n_too_large():
    head = list_to_linkedlist([1, 2, 3])
    with pytest.raises(ValueError):
        remove_nth_last_node(head, 5)

def test_n_equals_length():
    head = list_to_linkedlist([5, 6, 7, 8])
    new_head = remove_nth_last_node(head, 4)
    assert linkedlist_to_list(new_head) == [6, 7, 8]

def test_remove_last_two():
    head = list_to_linkedlist([1, 2, 3, 4])
    new_head = remove_nth_last_node(head, 2)
    assert linkedlist_to_list(new_head) == [1, 2, 4]
