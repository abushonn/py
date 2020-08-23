class Node:
    def __init__(self, data=None):
        self.value = data
        self.left = None
        self.right = None

    def __str__(self):
            return self.value

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if (self.root == None):
            self.root = Node(value)
            was_added = True
        else:
            was_added = self._insert(value, self.root)
            return was_added

    def _insert(self, value, node):
        was_added = False
        if (value < node.value):
            if (node.left == None):
                node.left = Node(value)
                was_added = True
            else:
                was_added = self._insert(value, node.left)
        elif (value > node.value):
            if (node.right == None):
                node.right = Node(value)
                was_added = True
            else:
                was_added = self._insert(value, node.right)
        else: #already exists in tree
            print('Value {} already in tree'.format(value))

        return was_added

    def print_tree_in_order(self):
        if (self.root != None):
            self._print_tree_in_order(self.root)

    def _print_tree_in_order(self, node):
        if (node != None):
            self._print_tree_in_order(node.left)
            print (str(node.value))
            self._print_tree_in_order(node.right)

    def fill_tree(self, num_elems = 10, max_int=100):
        from random import randint
        for i in range(0, num_elems):
            elem=randint(0, max_int)
            was_added = self.insert(elem)
            if (was_added):
                print('Element {} was added to tree'.format(elem))


print('============ Test Tree Create =================')
tree = BST()
tree.fill_tree()
tree.print_tree_in_order()