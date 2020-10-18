'''main.py CS2420 Project 5 Luis Gago: No help from other students.'''
from binarysearchtree import BinarySearchTree
from binarysearchtree import Node

def main():
    '''main function'''
    vals = [21, 26, 30, 9, 4, 14, 28, 18, 15, 10, 2, 3, 7]
    bst = BinarySearchTree()
    for val in vals:
        bst.add(val)
    print(', '.join(map(str, bst.preorder())) + ",")
    print(bst)
    rems = [21, 9, 4, 18, 15, 7]
    for rem in rems:
        bst.remove(rem)
    print(bst)

if __name__ == "__main__":
    main()
