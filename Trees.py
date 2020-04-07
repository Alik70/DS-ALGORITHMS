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


def insert_left(root, newBranch):
    t = root.pop(2)

    if len(t) > 1:
        root.inserted(2, [newBranch, t, []])
    else:
        root.inserted(2, [newBranch, [], []])

    return root


