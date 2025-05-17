from linkedlist import LinkedList, print_list_with_forward_arrow

def remove_nth_last_node(head, n):
    left, right = head, head
    diff = n
    # creating the diff bw left and right
    while diff >0:
        # when right is already at last 
        if right.next == None:
            head = left.next
            return head
        right = right.next
        diff -= 1
    # moving both pointer the last 
    while right.next:
        left = left.next
        right = right.next
    # removing the node
    left.next = left.next.next
    return head

def main():
    lists = [[23, 89, 10, 5, 67, 39, 70, 28], [34, 53, 6, 95, 38, 28, 17, 63, 16, 76], [288, 224, 275, 390, 4, 383, 330, 60, 193],
    [1, 2, 3, 4, 5, 6, 7, 8, 9], [69, 8, 49, 106, 116, 112, 104, 129, 39, 14, 27, 12]]
    n = [4, 1, 6, 9, 11]
    # lists = [[23, 89, 10, 5, 67, 39, 70, 28], [34, 53, 6, 95, 38, 28, 17, 63, 16, 76]]
    # n = [4, 3]

    for i in range(len(n)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(lists[i])
        print(i+1, ". Linked List:\t", end='')
        print_list_with_forward_arrow(input_linked_list.head)
        print()
        print("n = ", n[i])
        result = remove_nth_last_node(input_linked_list.head, n[i])
        print("Updated Linked List:\t", end='')
        print_list_with_forward_arrow(result)
        print()
        print("-"*100)

if __name__ == '__main__':
    main()