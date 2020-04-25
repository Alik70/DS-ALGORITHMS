from datastructures.StacksDQ import Stack, Queue, Dequeue
from datastructures.Trees import *

s = Stack()
# print(s.isEmpty())
# s.push('1')
# s.push('two')
# s.push(True)
# print(s.size())
# print(s.isEmpty())
# print(s.pop())
# print("peek %s" % s.peek())

q = Queue()
# print(q.isEmpty(), q.size())
# q.enqueue('first')
# q.enqueue('second')
# q.enqueue('third')
#
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())

d = Dequeue()
# d.add_front('hello')
# d.add_rear("world")
# print(d.items)
# print(d.size())
# print(d.remove_front(), d.remove_rear())
# print(d.size())


# a = Node(1)
# b = Node(2)
# c = Node(3)
# a.next_node = b
# b.next_node = c
# print(a.next_node.value)
# print(b.next_node.value)


# a = DoublyLinkedList(1)
# b = DoublyLinkedList(2)
# c = DoublyLinkedList(3)
#
# a.next_node = b
# b.prev_node = a
# b.next_node = c
# c.prev_node = b
#
# print(b.prev_node.value, c.prev_node.value, a.next_node.value)

# print(factoriel(99))
# print(add_fact(10))
# print(sum_func(12345))

# r = binary_tree(3)
# print(r)
# insert_left(r, 4)
# print(r)
# insert_left(r, 5)
# print(r)
# insert_right(r, 6)
# print(r)
# insert_right(r, 7)
# print(r)
# print(get_left_child(r))
# set_root_value(get_left_child(r), 9)
# print(r)

r = BinaryTree('a')
print(r.key)
r.insert_left('b')
r.insert_right('c')
print(r.get_left_child().key, r.get_right_child().key)
