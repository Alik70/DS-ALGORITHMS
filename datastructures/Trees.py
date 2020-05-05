# Tree implementation with classes

class BinaryTree(object):

    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None

    def insert_left(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insert_right(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def get_right_child(self):
        return self.rightChild

    def get_left_child(self):
        return self.leftChild

    def set_root_value(self, value):
        self.key = value

    def get_root_value(self):
        return self.key


# Tree list implementation

def binary_tree(r):
    return [r, [], []]


def insert_left(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])

    return root


def insert_right(root, newBranch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])

    return root


def get_root_val(root):
    return root[0]


def set_root_value(root, val):
    root[0] = val


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


def pre_order(tree):
    if tree:
        print(tree.get_root_value)
        pre_order(tree.get_left_child())
        pre_order(tree.get_right_child())


def post_order(tree):
    if tree:
        post_order(tree.get_left_child())
        post_order(tree.get_right_child())
        print(tree.get_root_value())


def in_order(tree):
    if tree:
        in_order(tree.get_left_child)
        print(tree.get_root_value())
        in_order(tree.get_right_child())

