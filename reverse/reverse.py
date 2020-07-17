class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev = None):
        # while node is not None
        while node:
            # set next node for while loop
            next_n = node.next_node
            # reverse node and next node
            node.next_node = prev
            prev = node
            # update node to loop again
            node = next_n
        # update list head
        self.head = prev

        # if node:
        #     next_n = node.next_node
        #     node.next = prev
        #     prev = node
        #     node = next_n
        # self.reverse_list(node, prev)
        # self.head = prev

if __name__ == "__main__":
    my_list = LinkedList()
    my_list.add_to_head(1)
    my_list.add_to_head(2)
    my_list.add_to_head(3)
    my_list.reverse_list(my_list.head, None)
