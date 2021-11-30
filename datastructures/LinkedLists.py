class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None


# NODE
class DoublyLinkedList(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

