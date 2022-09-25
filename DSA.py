################################## Data Structures ################################

# ------------------------------- Singly Linked List -----------------------------

class SinglyLinkedListNode:
    """ SinglyLinkedListNode
        Data structure for a singly linked list node
        Has two member variables:

        1. data (to store data)
        2. next (pointer to next node)

        | Has one constructors and one converter:
        | __init__(self, data)
        | __str__(self)

    """
    def __init__(self, data):
        """Default constructor for a linked list node

        :param data: The data to be stored
        :param next: Pointer to the next node

        >>> from DSA import SinglyLinkedListNode
        >>> a = 65
        >>> node = SinglyLinkedListNode(a)
        >>> print(node.data)
        65
        >>> print(type(node.data))
        <class 'int'>
        """
        self.data = data
        self.next = None
    
    def __str__(self):
        """Converter method which converts data stored in the
        node to a string and returns it

        >>> print(str(node.data))
        65
        >>> print(type(str(node.data)))
        <class 'str'>
        """
        return str(self.data)

class SinglyLinkedList:
    """ Data structure of the singly linked list

    | Contains two pointers, head and tail and member variables, pointing to linked list nodes
    | Contains the following member functions:

    * __init__(self)
    * insert(self, data)
    * find(self, data)
    * deleteVal(self, data)
    * printer(self, sep = ', ')
    * reverse(self)

    """
    def __init__(self):
        """ Constructor for the Singly Linked List, sets the head and tail to None

        >>> from DSA import SinglyLinkedList
        >>> L = SinglyLinkedList()
        >>> print(L.head)
        None
        >>> print(L.tail)
        None
        """
        self.head = None
        self.tail = None
   
    def insert(self, data):
        """Insert function, inserts nodes into the linked list, storing the data

        :param data: The data to be stored in the linked list

        >>> L.insert(10)
        >>> L.insert(12)
        >>> L.insert(25)
        >>> print(L.head)
        10
        >>> print(L.tail)
        25
        """
        node = SinglyLinkedListNode(data) # new node
        if not self.head: # no head
            self.head = node
        else:
            self.tail.next = node # add behind tail
        self.tail = node # move tail
    
    def find(self, data):
        """Finds if a value is stored in the linked list or not

        :param data: The value to be found in the linked list
        :return: The previous node, if the first node is to be found, returns None, and if the value is not in the list, returns the last node
        :rtype: SinglyLinkedListNode or Nonetype
        
        >>> print(L.find(10))
        None
        >>> print(L.find(12))
        10
        >>> print(L.find(25))
        12
        """
        head = self.head
        prev = None
        while head != None and head.data != data:
            prev = head
            head = head.next
        return prev
    
    def deleteVal(self, data):
        """Deletes values from the linked list

        :param data: The value to be deleted
        :returns: True, if the value was successfully deleted, otherwise False
        :rtype: bool

        >>> L = SinglyLinkedList()
        >>> L.insert(10)
        >>> L.insert(12)
        >>> L.insert(25)
        >>> L.deleteVal(13) 
        False
        >>> L.deleteVal(25)
        True
        """
        prevPos = self.find(data)
        if prevPos == None:
            if prevPos.next == None:
                return False
            self.head = prevPos.next
            return True
        elif prevPos.next == None:
            return False
        prevPos.next.next = prevPos.next
        return True
    
    def printer(self, sep=', '):
        """Prints the Linked List

        :param sep: The separator will be printed in between the values in the linked list

        >>> L = SinglyLinkedList()
        >>> L.insert(10)
        >>> L.insert(12)
        >>> L.insert(25)
        >>> L.printer(':')
        [10:12:25]
        """
        ptr = self.head
        print('[', end='')
        while ptr != None:
            print(ptr, end='')
            ptr = ptr.next
            if ptr != None:
                print(sep, end='')
        print(']')
    
    def reverse(self):
        """Reverses the whole linked list

        >>> L = SinglyLinkedList()
        >>> L.insert(10)
        >>> L.insert(12)
        >>> L.insert(25)
        >>> L.printer()
        [10, 12, 25]
        >>> L.reverse()
        >>> L.printer()
        [25, 12, 10]
        """
        head = self.head # head pointer
        prev = None # previous pointer
        while head != None: # while there is forward link left
            newHead = head.next # save extra pointer to next element
            head.next = prev # reverse the link of current element
            prev = head # move pointer to previous element
            head = newHead # use extra pointer to move to next element
        self.tail = self.head
        self.head = prev

def merge(list1, list2):
    """Merges two linked lists together

    :param list1: The first list to be merged
    :param list2: The second list to be merged
    :return: Returns the merged Linked list
    :rtype: SinglyLinkedList

    >>> from DSA import merge, SinglyLinkedList
    >>> L1 = SinglyLinkedList()
    >>> L1.insert(10)
    >>> L1.insert(12)
    >>> L1.insert(25)
    >>> L1.printer()
    [10, 12, 25]
    >>> L2 = SinglyLinkedList()
    >>> L2.insert(67)
    >>> L2.insert(100)
    >>> L2.insert(26)
    >>> L2.printer()
    [67, 100, 26]
    >>> L3 = merge(L1, L2)
    >>> L3.printer()
    [10, 12, 25, 67, 100, 26]
    """
    merged = SinglyLinkedList()
    head1 = list1.head
    head2 = list2.head
    while head1 != None and head2 != None: # both lists not empty
        if head1.data < head2.data: # link node with smaller data
            merged.insert(head1.data)
            head1 = head1.next
        else:
            merged.insert(head2.data)
            head2 = head2.next
    if head1 == None and head2 != None: # list 1 finished
        merged.tail.next = head2 # add remaining list 2 as is
    if head1 != None and head2 == None: # list 2 finished
        merged.tail.next = head1 # add remaining list 1 as is
    return merged

# ------------------------------ Doubly Linked List ----------------------------

class DoublyLinkedListNode:
    """ DoublyLinkedListNode
        Data structure for a Doubly linked list node

        | Has two member variables:
        | data (to store data)
        | next (pointer to next node)
        | prev (pointer to the previous node)

        | Has one constructors and one converter:
        | __init__(self, data)
        | __str__(self)

    """
    
    def __init__(self, data):
        """Default constructor for a linked list node

        :param data: The data to be stored
        :param next: Pointer to the next node
        :param prev: Pointer to the previous node

        >>> from DSA import DoublyLinkedListNode
        >>> a = 65
        >>> node = DoublyLinkedListNode(a)
        >>> print(node.data)
        65
        """
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self):
        """Converter method which converts data stored in the
        node to a string and returns it

        >>> print(str(node.data))
        65
        >>> print(type(str(node.data)))
        <class 'str'>
        """
        return str(self.data) 

class DoublyLinkedList:
    """ Data structure of the Doubly linked list

    | Contains two pointers, head and tail and member variables, pointing to linked list nodes
    | Contains the following member functions:
    | __init__(self)
    | insert(self, data)
    | printer(self, sep = ', ')
    | reverse(self)

    """
    def __init__(self):
        """ Constructor for the Singly Linked List, sets the head and tail to None

        >>> from DSA import DoublyLinkedList
        >>> L = DoublyLinkedList()
        >>> print(L.head)
        None
        >>> print(L.tail)
        None
        """
        self.head = None
        self.tail = None
    
    def insert(self, data):
        """Insert function, inserts nodes into the linked list, storing the data

        :param data: The data to be stored in the linked list

        >>> L.insert(10)
        >>> L.insert(12)
        >>> L.insert(25)
        >>> print(L.head)
        10
        >>> print(L.tail)
        25
        >>> L.insert(26)
        >>> print(L.tail)
        26
        """
        node = DoublyLinkedListNode(data) # new node
        if not self.head: # no head
            self.head = node
        else:
            self.tail.next = node # add behind tail
            node.prev = self.tail
        self.tail = node # move tail
    
    def printer(self, sep=', '):
        """Prints the Linked List

        :param sep: The separator will be printed in between the values in the linked list

        >>> L.printer(':')
        [10:12:25:26]
        >>> L.insert(27)
        >>> L.printer()
        [10, 12, 25, 26, 27]
        """
        ptr = self.head
        print('[', end='')
        while ptr != None:
            print(ptr, end='')
            ptr = ptr.next
            if ptr != None:
                print(sep, end='')
        print(']')
    
    def reverse(self):
        """Reverses the whole linked list

        >>> L.printer()
        [10, 12, 25, 26, 27]
        >>> L.reverse()
        >>> L.printer()
        [27, 26, 25, 12, 10]
        >>> L.insert(34)
        >>> L.reverse()
        >>> L.printer()
        [34, 10, 12, 25, 26, 27]
        """
        head = self.head # head pointer
        prev = None # previous pointer
        while head != None: # new node left
            newHead = head.next # save pointer to next node (cut forward link)
            if newHead != None: # check if next node has a reverse link
                newHead.prev = head # save pointer to previous node (cut reverse link)
            head.next = prev # reverse the forward link
            head.prev = newHead # reverse the reverse link
            prev = head # move pointer to previous element
            head = newHead # use saved pointer to move head
        self.tail = self.head
        self.head = prev

# -------------------------- Binary Search Tree ------------------------------


class BSTNode:
    """Data Structure for a Binary Search Tree Node

    | The member variables are:
    | info
    | level (storing the data and the level of the node)
    | left (pointer to left child)
    | right (pointer to right child)
    
    | The member functions are:
    | __init__(self, info)
    | __str__(self)

    """
    def __init__(self, info):
        """Constructor for BSTNode, initialises the data stored in the node,
        the pointers left and right are made None, and the level is set to None

        >>> from DSA import BSTNode
        >>> node = BSTNode(69)
        >>> print(node.info)
        69
        """
        self.info = info
        self.left = None
        self.right = None
        self.level = None
    
    def __str__(self):
        """Converts the data stored in the node to a string

        :return: The data stored converted to string
        :rtype: string

        >>> print(str(node))
        69
        """
        return str(self.info)

class BinarySearchTree:
    """Data Structure of a Binary Search Tree
    
    | The member variables are:
    | root (the root of the tree)

    | The member functions are:
    | __init__(self)
    | insert(self, val)
    | traverse(self, order)
    | height(self, root)

    """
    # def __init__(self):
    #     """Constructor of the BinarySearchTree, sets the root to None

    #     >>> from DSA import BinarySearchTree
    #     >>> tree = BinarySearchTree()
    #     >>> print(tree.root)
    #     None
    #     """
    #     self.root = None
    
    # def insert(self, val):
    #     """Insert data into the BST

    #     :param val: The value to be inserted in the BST

    #     >>> tree.insert(10)
    #     >>> tree.insert(4)
    #     >>> tree.insert(24)
    #     >>> print(tree.root)
    #     10
    #     >>> print(tree.root.left)
    #     4
    #     >>> print(tree.root.right)
    #     24
    #     """
    #     if self.root == None:
    #         self.root = BSTNode(val)
    #     else:
    #         current = self.root
    #         while True:
    #             if val < current.info: # move to left sub-tree
    #                 if current.left:
    #                     current = current.left # root moved
    #                 else:
    #                     current.left = BSTNode(val) # left init
    #                     break
    #             elif val > current.info: # move to right sub-tree
    #                 if current.right:
    #                     current = current.right # root moved
    #                 else:
    #                     current.right = BSTNode(val) # right init
    #                     break
    #             else:
    #                 break # value exists
    
    # def traverse(self, order):
    #     """Traverses the tree in the given order and prints it out

    #     :param order: Specifies the order in which the tree is to be traversed, can be PRE, IN or POST

    #     >>> tree.traverse('PRE')
    #     10 4 24 
    #     >>> tree.traverse('POST')
    #     4 24 10 
    #     >>> tree.traverse('IN')
    #     4 10 24 
    #     >>> tree.insert(64)
    #     >>> tree.traverse('POST') # doctest: +NORMALIZE_WHITESPACE
    #     4 64 24 10
    #     >>> tree.insert(20)
    #     >>> tree.traverse('PRE') # doctest: +NORMALIZE_WHITESPACE
    #     10 4 24 20 64

    #     Note that in the first few traversals, I have manually added a trailing whitespace, alternatively
    #     doctest flags can also be used as shown
    #     """
    #     def preOrder(root):
    #         print(root.info, end=' ')
    #         if root.left != None:
    #             preOrder(root.left)
    #         if root.right != None:
    #             preOrder(root.right)
    #     def inOrder(root):
    #         if root.left != None:
    #             inOrder(root.left)
    #         print(root.info, end=' ')
    #         if root.right != None:
    #             inOrder(root.right)
    #     def postOrder(root):
    #         if root.left != None:
    #             postOrder(root.left)
    #         if root.right != None:
    #             postOrder(root.right)
    #         print(root.info, end=' ')
    #     if order == 'PRE':
    #         preOrder(self.root)
    #     elif order == 'IN':
    #         inOrder(self.root)
    #     elif order == 'POST':
    #         postOrder(self.root)
    
    # def height(self, root):
    #     """Gives the height of the tree

    #     :param root: The node from which height is to be found
    #     :return: The height of the tree from the given node
    #     :rtype: int

    #     >>> node = tree.root
    #     >>> print(tree.height(node))
    #     2
    #     >>> print(tree.height(node.left))
    #     0
    #     >>> tree.insert(29)
    #     >>> print(tree.height(node))
    #     3
    #     """
    #     if root.left == None and root.right == None:
    #         return 0
    #     elif root.right == None:
    #         return 1 + self.height(root.left)
    #     elif root.left == None:
    #         return 1 + self.height(root.right)
    #     else:
    #         return 1 + max(self.height(root.left),self.height(root.right))

# --------------------------------- Suffix Trie --------------------------------

class Trie:
    """Data Structure of a Trie

    | Has member variables:
    | count
    | nodes

    | Has the following member functions:
    | __init__(self)
    | find(self, root, c)
    | insert(self, s)
    | checkPrefix(self, s)
    | countPrefix(self, s)

    """
    def __init__(self):
        """Constructor of Trie, creates an empty Trie

        >>> from DSA import Trie
        >>> t = Trie()
        >>> print(t.T)
        {}
        """
        self.T = {}
    
    def find(self, root, c):
        """Finds whether the node correctly corresponds to the character

        :param root: A node of the trie whose character is to be checked
        :param c: The character to be checked
        :return: True if they match, else False
        :rtype: bool

        >>> t.insert('banana')
        >>> root = t.T
        >>> print(t.find(root, 'a'))
        False
        >>> print(t.find(root, 'b'))
        True
        >>> print(t.find(root['b'], 'b'))
        False
        >>> print(t.find(root['b'], 'a'))
        True
        """
        return (c in root)
    
    def insert(self, s):
        """Inserts a word in the Trie
        :param s: The string to be inserted in the trie
        
        >>> t.insert('cat')
        >>> print(t.find(root, 'a'))
        False
        >>> print(t.find(root, 'b'))
        True
        >>> print(t.find(root, 'c'))
        True
        """
        root = self.T
        for c in s:
            if not self.find(root,c):
                root[c] = {}
            root = root[c]
            root.setdefault('#',0)
            root['#'] += 1
    
    def checkPrefix(self, s):
        """Checks if a word is a prefix of any word stored in the Trie

        :param s: The prefix to be checked
        :return: If the string is a prefix, then True, else False
        :rtype: bool

        >>> print(t.checkPrefix('ca'))
        True
        >>> print(t.checkPrefix('ban'))
        True
        >>> print(t.checkPrefix('bac'))
        False
        """
        root = self.T
        for idx, char in enumerate(s):
            if char not in root:
                if idx == len(s) - 1:    
                    root[char] = '#'
                else:
                    root[char] = {}
            elif root[char] == '#' or idx == len(s) - 1:
                return True
            root = root[char]
        return False
    
    def countPrefix(self, s):
        """ counts the number of words which have a string as the prefix

        :param s: The prefix to be checked
        :return: The number of times the prefix appears
        :rtype: int

        >>> print(t.countPrefix('ba'))
        1
        >>> t.insert('basketball')
        >>> t.insert('bandicam')
        >>> t.insert('bat')
        >>> print(t.countPrefix('ba'))
        4
        >>> print(t.countPrefix('ban'))
        2
        """
        found = True
        root = self.T
        for c in s:
            if self.find(root,c):
                root = root[c]
            else:
                found = False
                break
        if found:
            return root['#']
        return 0

# --------------------------------------Heap------------------------------------

class Heap:
    """ This Heap class is  a specialized tree-based data structure which is essentially an almost complete
    tree that satisfies the heap property: in a max heap, for any given node C, if P is a parent node of C,
    then the key (the value) of P is greater than or equal to the key of C. In a min heap, the key of P is
    less than or equal to the key of C.

    | The node at the "top" of the heap (with no parents) is called the root node. 
    | The functions in the class are:

    - __init__(self, cap)
    - parent(self, i)
    - left(self, i)
    - right(self, i)
    - insert(self, val)
    - min(self)
    - Heapify(self, root)
    - deleteMin(self)

      """
    def __init__(self, cap):
        """ Constructor for adding nodes in the heap

        :param cap: The value to be stored in the heap
        :type cap: numeric
        
        >>> from DSA import Heap
        >>> heap = Heap(10)
        >>> print(heap.M)
        10
        >>> print(heap.n)
        0
        >>> print(heap.H)
        []
        """
        self.H = []
        self.n = 0
        self.M = cap
    
    def parent(self, i):
        """Finds parent of a node

        :param i: The index of the node to find the parent of
        :type i: int
        :return: Returns the index of the parent
        :rtype: int
        
        >>> heap.insert(5)
        >>> heap.insert(2)
        >>> heap.insert(12)
        >>> heap.insert(29)
        >>> print(heap.H)
        [2, 5, 12, 29]
        >>> print(heap.parent(1))
        0
        >>> print(heap.parent(3))
        1
        """
        return (i - 1) // 2
    
    def left(self, i):
        """Finds left child of a node

        :param i: The index of the node to find the left of
        :type i: int
        :return: Returns the index of the left child
        :rtype: int

        >>> print(heap.left(0))
        1
        >>> print(heap.left(1))
        3
        >>> heap.insert(22)
        >>> heap.insert(43)
        >>> print(heap.left(2))
        5
        """
        return (2 * i) + 1
    
    def right(self, i):
        """Finds right child of a node

        :param i: The index of the node to find the right of
        :type i: int
        :return: Returns the index of the right child
        :rtype: int

        >>> print(heap.right(0))
        2
        >>> print(heap.right(1))
        4
        >>> heap.insert(22)
        >>> heap.insert(43)
        >>> heap.insert(56)
        >>> print(heap.right(2))
        6
        """
        return 2 * (i + 1)
    
    def insert(self, val):
        """Inserts new value in the heap

        :param val: new value to be inserted
        :type val: numeric

        >>> from DSA import Heap
        >>> heap = Heap(10)
        >>> heap.insert(5)
        >>> heap.insert(2)
        >>> heap.insert(12)
        >>> heap.insert(29)
        >>> print(heap.H)
        [2, 5, 12, 29]
        """
        if self.n != self.M:
            self.H.append(val)
            i = self.n
            self.n += 1
            while i != 0 and self.H[self.parent(i)] > self.H[i]:
                self.H[i], self.H[self.parent(i)] = self.H[self.parent(i)], self.H[i]
                i = self.parent(i)
    
    def min(self):
        """Finds min value in the heap

        :return: The min value stored, if the heap is non empty, else returns -1
        :rtype: int

        >>> print(heap.min())
        2
        >>> heap.insert(1)
        >>> print(heap.min())
        1
        """
        if (self.n != 0):
            return self.H[0]
        return -1
    
    def Heapify(self, root):
        """Performs self adjustment when the heap property is violated on addition of new values

        :param root: Root of the heap
        :type root: int

        | We'll purposely modify the list incorrectly and then heapify will correct it. 

        >>> print(heap.H)
        [1, 2, 12, 29, 5]
        >>> temp = heap.H[0]
        >>> heap.H[0] = heap.H[4]
        >>> heap.H[4] = temp
        >>> print(heap.H)
        [5, 2, 12, 29, 1]
        >>> heap.Heapify(0)
        >>> print(heap.H)
        [2, 1, 12, 29, 5]
        >>> heap.Heapify(0)
        >>> print(heap.H)
        [1, 2, 12, 29, 5]
        """
        l = self.left(root)
        r = self.right(root)
        s = root
        if (l < self.n and self.H[l] < self.H[root]):
            s = l
        if (r < self.n and self.H[r] < self.H[s]):
            s = r
        if s != root:
            self.H[root], self.H[s] = self.H[s], self.H[root]
            self.Heapify(s)
    
    def deleteMin(self):
        """Deletes min value in the heap

        >>> print(heap.H)
        [1, 2, 12, 29, 5]
        >>> heap.deleteMin()
        >>> print(heap.H)
        [2, 5, 12, 29, 5]
        >>> heap.deleteMin()
        >>> print(heap.H)
        [5, 29, 12, 29, 5]

        Note that the 0 and 1 at the end is technically deleted from the array, and as a new 
        element is inserted, it will be replaced
        """
        if self.n > 0:
            if self.n == 1:
                self.H = []
                self.n = 0
            else:
                self.n -= 1
                self.H[0] = self.H[self.n]
                self.Heapify(0)