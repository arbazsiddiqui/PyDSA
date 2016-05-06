class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    # return true if node points to another node
    def has_next(self):
        return self.next != None


class linked_list:
    def __init__(self):
        self.head = None

    def add_node_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_node_at_last(self, data):
        new_node = Node(data)
        current = self.head

        while current.next != None:
            current = current.next
        current.next = new_node

    def delete_first_node(self):
        self.head = self.head.next

    def delete_last_node(self):
        current_node = self.head
        previous_node = self.head

        while current_node.next != None:
            previous_node = current_node
            current_node = current_node.next

        previous_node.next = None

    def print_list(self):
        node_list = []
        current_node = self.head
        while current_node != None:
            node_list.append(current_node.data)
            current_node = current_node.next

        print node_list


ll = linked_list()
ll.add_node_at_beginning(9)
ll.add_node_at_beginning(3)
ll.add_node_at_beginning(2)
ll.add_node_at_beginning(4)
ll.add_node_at_last(5)
ll.delete_first_node()
ll.delete_last_node()
ll.print_list()
