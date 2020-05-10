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


class BinaryHeap(object):

    def __init__(self):
        self.heaplist = [0]
        self.currentsize = 0

    def min_child(self, i):
        if (i * 2) + 1 > self.currentsize:
            return i * 2
        else:
            if self.heaplist[i * 2] < self.heaplist[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def perc_down(self, i):
        while (i * 2) <= self.currentsize:
            mc = self.min_child(i)
            if self.heaplist[i] > self.heaplist[mc]:
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[mc]
                self.heaplist[mc] = tmp
            i = mc

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i // 2]:
                tmp = self.heaplist[i // 2]
                self.heaplist[i // 2] = self.heaplist[i]
                self.heaplist[i] = tmp
            i = i // 2

    def insert(self, item):
        self.heaplist.append(item)
        self.currentsize = self.currentsize + 1
        self.perc_up(self.currentsize)

    def del_min(self):
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentsize]
        self.currentsize = self.currentsize - 1
        self.heaplist.pop()
        self.perc_down(1)
        return retval

    def build_heap(self, hlist):
        i = len(hlist) // 2
        self.currentsize = len(hlist)
        self.heaplist = [0] + hlist[:]
        while (i > 0):
            self.perc_down(i)
            i = i - 1


class TreeNode(object):

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftchild = left
        self.rightchild = right
        self.parent = parent

    def has_left_child(self):
        return self.leftchild

    def has_right_child(self):
        return self.rightchild

    def is_left_child(self):
        return self.parent and self.parent.leftchild == self

    def is_right_child(self):
        return self.parent and self.parent.rightchild == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.leftchild and self.rightchild)

    def has_any_children(self):
        return self.rightchild or self.leftchild

    def has_both_children(self):
        return self.rightchild and self.leftchild

    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftchild = lc
        self.rightchild = rc
        if self.has_left_child():
            self.leftchild.parent = self
        if self.has_right_child():
            self.rightchild.parent = self


class BinarySearchTree(object):

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentnode):
        if key < currentnode.key:
            if currentnode.has_left_child():
                self._put(key, val, currentnode.leftchild)
            else:
                currentnode.leftchild = TreeNode(key, val, parent=currentnode)
        else:
            if currentnode.has_right_child():
                self._put(key, val, currentnode.rightchild)
            else:
                currentnode.rightchild = TreeNode(key, val, parent=currentnode)

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentnode):

        if not currentnode:
            return None
        elif currentnode.key == key:
            return currentnode
        elif key < currentnode.key:
            return self._get(key, currentnode.leftchild)
        else:
            return self._get(key, currentnode.rightchild)

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        if self._get(item, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError("Error, key not found in the tree.")

        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1

        else:
            raise KeyError("Error, key not found in the tree.")

    def __delitem__(self, key):
        self.delete(key)

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.leftchild = None
            else:
                self.parent.rightchild = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.leftchild = self.leftchild
        else:
            self.parent.rightchild = self.leftchild
            self.leftchild.parent = self.parent

    def find_successor(self):
        succ = None
        if self.has_right_child():
            succ = self.rightchild.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    succ = self.parent

                else:
                    self.parent.rightchild = None
                    succ = self.parent.find_successor()
                    self.parent.rightchild = self
        return succ

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.leftchild
        return current

    def remove(self, currentnode):

        if currentnode.is_leaf():
            if currentnode == currentnode.parent.leftchild:
                currentnode.parent.leftchild = None

            else:
                currentnode.parent.leftchild = None
        elif currentnode.has_both_children():
            succ = currentnode.find_successor()
            succ.splice_out()
            currentnode.key = succ.key
            currentnode.payload = succ.payload
        else:
            if currentnode.has_left_child():
                if currentnode.is_left_child():
                    currentnode.leftchild.parent = currentnode.parent
                    currentnode.parent.leftchild = currentnode.leftchild
                elif currentnode.is_right_child():
                    currentnode.leftchild.parent = currentnode.parent
                    currentnode.parent.rightchild = currentnode.leftchild
                else:
                    currentnode.replace_node_data(currentnode.leftchild.key,
                                                  currentnode.leftchild.payload,
                                                  currentnode.leftchild.leftchild,
                                                  currentnode.leftchild.rightchild
                                                  )
            else:
                if currentnode.is_left_child():
                    currentnode.rightchild.parent = currentnode.parent
                    currentnode.parent.leftchild = currentnode.rightchild
                elif currentnode.is_right_child():
                    currentnode.rightchild.parent = currentnode.parent
                    currentnode.parent.rightchild = currentnode.rightchild
                else:
                    currentnode.replace_node_data(currentnode.rightchild.key,
                                                  currentnode.rightchild.payload,
                                                  currentnode.rightchild.leftchild,
                                                  currentnode.rightchild.rightchild
                                                  )


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
