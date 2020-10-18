'''binarysearchtree.py CS2420 Project 5 Luis Gago: No help from other students.'''
from recursioncounter import RecursionCounter

class Node():
    '''class to declare binary tree nodes'''

    def __init__(self, data, left_child=None, right_child=None):
        '''initialize binary search tree node'''
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
        self.height = 0

    def is_leaf(self):
        '''return true if the node is a leaf false otherwise'''
        return self.left_child is None and self.right_child is None

    def update_height(self):
        '''update the node height.'''
        if self.is_leaf():
            return 0

        elif self.left_child is not None and self.right_child is None:
            return self.left_child.height + 1

        elif self.right_child is not None and self.left_child is None:
            return self.right_child.height + 1

        elif self.right_child is not None and self.left_child is not None:
            return max(self.right_child.height, self.left_child.height) + 1

    def __str__(self):
        '''function for printing nodes'''
        return str(str(self.data) + "(" + str(self.height) + ")")
        

class BinarySearchTree():
    '''class to create binary tree'''

    def __init__(self):
        '''initialize binary tree'''
        self.root = None

    def is_empty(self):
        '''return true if tree is empty false otherwise'''
        return self.root is None

    def add(self, data):
        '''add an item to the tree'''
        self.root = self.add_helper(self.root, data)
        return None

    def add_helper(self, cursor, data):
        '''helps the add function'''
        RecursionCounter()
        if cursor is None:
            return Node(data)
        if data > cursor.data:
            cursor.right_child = self.add_helper(cursor.right_child, data)
            cursor.height = cursor.update_height()
        elif data == cursor.data:
            return None
        else:
            cursor.left_child = self.add_helper(cursor.left_child, data)
            cursor.height = cursor.update_height()
        return cursor

    def find(self, data):
        '''find a node in a binary tree'''
        return self.find_helper(self.root, data)

    def find_helper(self, cursor, data):
        '''obfuscates the find function'''
        RecursionCounter()
        if cursor.data == data:
            return cursor
        elif cursor.left_child is None and cursor.right_child is None:
            return None
        elif cursor.data > data:
            self.find_helper(cursor.left_child, data)
        else:
            self.find_helper(cursor.right_child, data)

    def remove(self, data):
        '''removes an item from the tree'''
        self.root = self.remove_helper(self.root, data)
        self.rebalance_tree()
        return None

    def remove_helper(self, cursor, data):
        '''obfuscates the remove function'''
        RecursionCounter()
        if cursor == None:
            return None
        elif cursor.data == data:
            if cursor.is_leaf():
                # cursor = None
                return None
            if cursor.right_child is None and cursor.left_child is not None:
                # cursor = cursor.left_child
                cursor.height -= cursor.update_height()
                return cursor.left_child
            if cursor.left_child is None and cursor.right_child is not None:
                # cursor = cursor.right_child
                cursor.height -= cursor.update_height()
                return cursor.right_child
            if cursor.left_child is not None and cursor.right_child is not None:
                temp = cursor.right_child
                while temp.left_child is not None:
                    temp = temp.left_child
                cursor.data = temp.data
                cursor.right_child.height -= cursor.right_child.update_height()
                cursor.right_child = self.remove_helper(cursor.right_child, temp.data)
        elif data > cursor.data:
                cursor.right_child = self.remove_helper(cursor.right_child, data)
        elif data < cursor.data:
                cursor.left_child = self.remove_helper(cursor.left_child, data)
        cursor.height = cursor.update_height()
        return cursor

    def preorder(self):
        '''root->left->right'''
        output = ""
        output = self.preorder_helper(self.root, output)
        output = output.split("-")
        output = output[:-1]
        output = [int(i) for i in output]
        return output

    def preorder_helper(self, cursor, output):
        '''used to help preorder traversal'''
        RecursionCounter()
        if cursor:
            output += (str(cursor.data) + "-")
            output = self.preorder_helper(cursor.left_child, output)
            output = self.preorder_helper(cursor.right_child, output)
        return  output

    def height(self):
        '''returns the height of the binary tree'''
        if self.root:
            return self.root.height
        else:
            return -1

    def __str__(self):
        '''returns a string of the binary tree'''
        return self.print_helper(self.root, 0)

    def print_helper(self, cursor, offset):
        '''obfuscates the __str__ function'''
        RecursionCounter()
        final = ""
        if cursor:
            if cursor.is_leaf():
                final += ((" " * offset) + str(cursor.__str__()) + "[leaf]" + "\n")
            else:
                final += ((" " * offset) + str(cursor.__str__()) + "\n")
                final += self.print_helper(cursor.left_child, offset + 1)
                final += self.print_helper(cursor.right_child, offset + 1)
        else:
            final += ((" " * offset) + "[Empty]" + "\n")
        return final


    def __len__(self):
        '''returns the length of the tree'''
        if self.root:
            return self.length_helper(self.root, 0)
        else:
            return 0

    def length_helper(self, cursor, offset):
        '''obfuscates the length function'''
        RecursionCounter()
        if cursor is None:
            return 0
        return 1 + self.length_helper(cursor.left_child, 0) + self.length_helper(cursor.right_child, 0)
    
    def inorder(self):
        '''returns an in order list of items from BST'''
        return self.inorder_helper(self.root)


    def inorder_helper(self, root):
        '''obfuscates inorder'''
        inorder_list = list()
        if root:

            # First recur on left child
            inorder_list += self.inorder_helper(root.left_child)

            # append the data of node
            inorder_list.append(root.data)

            # now recur on right child
            inorder_list += self.inorder_helper(root.right_child)

        return inorder_list

    def rebalance_tree(self):
        '''rebalances a binary search tree'''
        empty_list = list()
        self.root = self.rebalance_tree_helper(self.root, empty_list)
        return None

    def rebalance_tree_helper(self, cursor, list_value):
        '''obfuscates the rebalance_tree function'''
        if len(list_value) == 0:
            list_value = self.inorder()
        middle_position = int(len(list_value)//2)
        middle_value = list_value[middle_position]
        left_half = list_value[:middle_position]
        right_half = list_value[middle_position + 1:]
        cursor = Node(middle_value)
        if len(left_half) != 0:
            cursor.left_child = self.rebalance_tree_helper(cursor.left_child, left_half)
        if len(right_half) != 0:
            cursor.right_child = self.rebalance_tree_helper(cursor.right_child, right_half)
        cursor.height = cursor.update_height()
        return cursor
