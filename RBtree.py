"""
Project 3 (Fall 2020) - Red/Black Trees
Name: Solution
"""
from __future__ import annotations
import queue
from typing import TypeVar, Generic, Callable, Generator
from copy import deepcopy
from Project3.RBnode import RBnode as Node

T = TypeVar('T')


class RBtree:
    """
    A Red/Black Tree class
    :root: Root Node of the tree
    :size: Number of Nodes
    """

    __slots__ = ['root', 'size']

    def __init__(self, root: Node = None):
        """ Initializer for an RBtree """
        # this alllows us to initialize by copying an existing tree
        self.root = deepcopy(root)
        if self.root:
            self.root.parent = None
        self.size = 0 if not self.root else self.root.subtree_size()

    def __eq__(self, other: RBtree) -> bool:
        """ Equality Comparator for RBtrees """
        comp = lambda n1, n2: n1 == n2 and \
            ((comp(n1.left, n2.left) and \
                comp(n1.right, n2.right)) if (n1 and n2) else True)
        return comp(self.root, other.root) and self.size == other.size

    def __str__(self) -> str:
        """ represents Red/Black tree as string """

        if not self.root:
            return 'Empty RB Tree'

        root, bfs_queue, height = self.root, queue.SimpleQueue(), self.root.subtree_height()
        track = {i:[] for i in range(height+1)}
        bfs_queue.put((root, 0, root.parent))

        while bfs_queue:
            n = bfs_queue.get()
            if n[1] > height:
                break
            track[n[1]].append(n)
            if n[0] is None:
                bfs_queue.put((None, n[1]+1, None))
                bfs_queue.put((None, n[1]+1, None))
                continue
            bfs_queue.put((None, n[1]+1, None) if not n[0].left else (n[0].left, n[1]+1, n[0]))
            bfs_queue.put((None, n[1]+1, None) if not n[0].right else (n[0].right, n[1]+1, n[0]))

        spaces = 12*(2**(height))
        ans = '\n' + '\t\tVisual Level Order Traversal of RBtree'.center(spaces) + '\n\n'
        for i in range(height):
            ans += f"Level {i+1}: "
            for n in track[i]:
                space = int(round(spaces / (2**i)))
                if not n[0]:
                    ans += ' ' * space
                    continue
                ans += "{} ({})".format(n[0], n[2].value if n[2] else None).center(space, " ")
            ans += '\n'
        return ans

    def __repr__(self) -> str:
        return self.__str__()

################################################################
################### Complete Functions Below ###################
################################################################

######################## Static Methods ########################
# These methods are static as they operate only on nodes, 
# without explicitly referencing an RBtree instance

    @staticmethod
    def set_child(parent: Node, child: Node, is_left: bool) -> None:
        """
        Sets the child parameter of parent to child.
        Time Complexity: O(1), Space Complexity: O(1)
        """
        if is_left:
            parent.left = child
        else:
            parent.right = child
        if child:
            child.parent = parent

    @staticmethod
    def replace_child(parent: Node, current_child: Node, new_child: Node) -> None:
        """
        Replaces parents child current_child with new_child
        Time Complexity: O(1), Space Complexity: O(1)
        """
        if current_child == parent.right:
            return RBtree.set_child(parent, new_child, False)
        else:
            return RBtree.set_child(parent, new_child, True)

    @staticmethod
    def get_sibling(node: Node) -> Node:
        """
        Return the other child of the node's parent
        Time Complexity: O(1), Space Complexity: O(1)
        """
        if not node.parent: #no parent exists
            return
        if node == node.parent.left:
            return node.parent.right
        return node.parent.left

    @staticmethod
    def get_grandparent(node: Node) -> Node:
        """
        Given a node, returns the parent of that node's parent, or None should no such node exist.
        Time Complexity: O(1), Space Complexity: O(1)
        """
        if not node.parent:
            return
        return node.parent.parent

    @staticmethod
    def get_uncle(node: Node) -> Node:
        """
        Given a node, returns the sibling of that node's parent, or None should no such node exist.
        Time Complexity: O(1), Space Complexity: O(1)
        """
        if not node.parent:
            return
        if not node.parent.parent:
            return
        if node.parent == node.parent.parent.left:
            return node.parent.parent.right
        return node.parent.parent.left

 ######################## Misc Utilities ##########################

    def min(self, node: Node) -> Node:
        """
        Returns the minimum value stored in the subtree rooted at node. \
            (None if the subtree is empty).
        Time Complexity: O(log(n)), Space Complexity: O(1)
        """
        if not node:
            return None
        while node.left is not None:
            node = node.left
        return node

    def max(self, node: Node) -> Node:
        """
        Returns the maximum value stored in a subtree rooted at node. \
            (None if the subtree is empty).
        Time Complexity: O(log(n)), Space Complexity: O(1)
        """
        if not node:
            return None
        while node.right is not None:
            node = node.right
        return node

    def search(self, node: Node, val: Generic[T]) -> Node:
        """
        Searches the subtree rooted at node for a node containing value val. \
            If such a node exists, return that node- otherwise return the node \
                which would be parent to a node with value val should such a node be inserted.
        Time Complexity: O(log(n)), Space Complexity: O(1)
        """
        if not node:
            return
        if node.value == val: #desired node searched
            return node
        #Recursive function to reach O(log(n))
        if node.right and node.value < val:
            return self.search(node.right, val)
        if node.left and node.value > val:
            return self.search(node.left, val)
        return node

 ######################## Tree Traversals #########################

    def inorder(self, node: Node) -> Generator[Node, None, None]:
        """
        Returns a generator object describing an inorder traversal of the subtree rooted at node.
        Time Complexity: O(n), Space Complexity: O(n)
        """
        #Referenced from Zybook Chapter 24.7
        if not node:
            return None
        yield from self.inorder(node.left)#L
        yield node#cur
        yield from self.inorder(node.right)#R

    def preorder(self, node: Node) -> Generator[Node, None, None]:
        """
        Returns a generator object describing a preorder traversal of the subtree rooted at node.
        Time Complexity: O(n), Space Complexity: O(n)
        """
        if not node:
            return None
        yield node
        yield from self.preorder(node.left)
        yield from self.preorder(node.right)

    def postorder(self, node: Node) -> Generator[Node, None, None]:
        """
        Returns a generator object describing a postorder traversal of the subtree rooted at node.
        TIme Complexity: O(n), Space Complexity: O(n)
        """
        if not node:
            return None
        yield from self.postorder(node.left)
        yield from self.postorder(node.right)
        yield node

    def bfs(self, node: Node) -> Generator[Node, None, None]:
        """
        Returns a generator object describing a breadth first traversal \
            of the subtree rooted at node.
        Time Complexity: O(n), Space Complexity: O(n)
        """
        #Athogirithm like binary search
        if not node:
            return None
        queue_RBtree = queue.Queue()
        queue_RBtree.put(node)
        while queue_RBtree.qsize() != 0:
            temp_node = queue_RBtree.get()
            yield temp_node
            #Tracking the trace
            if not temp_node:
                return None
            if temp_node.left is not None:
                queue_RBtree.put(temp_node.left)
            if temp_node.right is not None:
                queue_RBtree.put(temp_node.right)

 ################### Rebalancing Utilities ######################

    def left_rotate(self, node: Node) -> None:
        """
        Performs a left tree rotation on the subtree rooted at node.
        Time Complexity: O(1), Space Complexity: O(1)
        """
        # Referenced from Zybook Chapter 25.6
        rightLeftChild = node.right.left
        if node.parent != None:
            RBtree.replace_child(node.parent, node, node.right)
        else: #node is root
            self.root = node.right
            self.root.parent = None
        RBtree.set_child(node.right, node, True)
        RBtree.set_child(node, rightLeftChild, False)

    def right_rotate(self, node: Node) -> None:
        """
        Performs a right tree rotation on the subtree rooted at node.
        Time Complexity: O(1), Space Complexity: O(1)
        """
        # Referenced from Zybook Chapter 25.6
        leftRightChild = node.left.right
        if node.parent != None:
            RBtree.replace_child(node.parent, node, node.left)
        else: #node is root
            self.root = node.left
            self.root.parent = None
        RBtree.set_child(node.left, node, False)
        RBtree.set_child(node, leftRightChild, True)

    def insertion_repair(self, node: Node) -> None:
        """
        Rebalance the tree by ensuring adherance to Red/Black properties.
        Time Complexity: O(log(n)), Space Complexity: O(1)
        """
        #Cite Zybook From 25.7 Red-black tree: Insertion
        if node.parent is None:
            node.is_red = False
            return
        # Balanced the tree
        if not node.parent.is_red:
            if (node.right and not node.right.is_red) or (node.left and not node.left.is_red):
                node.is_red = True
            return
        uncle = RBtree.get_uncle(node)
        parent = node.parent
        grandpa = RBtree.get_grandparent(node)
        if uncle and uncle.is_red == True:
            parent.is_red = uncle.is_red = False
            grandpa.is_red = True
            self.insertion_repair(grandpa)
            return
        if node == parent.right and parent == grandpa.left:
            self.left_rotate(parent)
            node = parent
            parent = node.parent
        elif node == parent.left and parent == grandpa.right:
            self.right_rotate(parent)
            node = parent
            parent = node.parent
        parent.is_red = False
        grandpa.is_red = True
        if node == parent.left:
            self.right_rotate(grandpa)
        else:
            self.left_rotate(grandpa)

    def prepare_removal(self, node: Node) -> None:
        """
        Ensure balance is maintained after the removal.
        Time Complexity: O(log(n)), Space Complexity: O(1)
        """
        #Cite From zybooks 25.8 Red-black tree: Removal
        sib = self.get_sibling(node)
        def AreBothChildBlack(node: Node):
            """
            Returns true only if both of a node's children are black
            """
            if node.left and node.left.is_red:
                return False
            if node.right and node.right.is_red:
                return False
            return True
        def IsNoNoneAndRed(node: Node):
            """
            Returns true only if a node is non-null and red
            """
            if not node:
                return False
            return node.is_red == True
        def IsNoneOrBlack(node: Node):
            """
            Returns true if a node is null or black
            """
            if not node:
                return True
            return node.is_red == False

        def RBTreeCase1(node: Node):
            #Node is red or node's parent is null.
            if node.is_red or not node.parent:
                return True
            else:
                return False
        def RBTreeCase2(node: Node, sib: Node):
            #Sibling node is red.
            if sib.is_red:
                node.parent.is_red = True
                sib.is_red = False
                if node == node.parent.left:
                    self.left_rotate(node.parent)
                else:
                    self.right_rotate(node.parent)
                return True
            return False
        def RBTreeCase3(node: Node, sib: Node):
            #Parent is black and both of sibling's children are black.
            if not node.parent.is_red and AreBothChildBlack(sib):
                sib.is_red = True
                self.prepare_removal(node.parent)
                return True
            return False
        def RBTreeCase4(node: Node, sib: Node):
            #Parent is red and both of sibling's children are black.
            if node.parent.is_red and AreBothChildBlack(sib):
                node.parent.is_red = False
                sib.is_red = True
                return True
            return False
        def RBTreeCase5(node: Node, sib: Node):
            #Sibling's left child is red, sibling's right child is black, \
            #and node is left child of parent.
            if IsNoNoneAndRed(sib.left) and IsNoneOrBlack(sib.right) \
                and node == node.parent.left:
                sib.is_red = True
                sib.left.is_red = False
                self.right_rotate(sib)
                return True
            return False
        def RBTreeCase6(node: Node, sib: Node):
            #Sibling's left child is black, sibling's right child is red, \
            #and node is right child of parent.
            if IsNoNoneAndRed(sib.right) and IsNoneOrBlack(sib.left) \
                and node == node.parent.right:
                sib.is_red = True
                sib.right.is_red = False
                self.left_rotate(sib)
                return True
            return False

        if RBTreeCase1(node):
            """
            None
            """
            return
        if RBTreeCase2(node, sib):
            """
            Color parent red and sibling black. If node is left child of parent, \
                rotate left at parent node, otherwise rotate right at parent node
            """
            sib = self.get_sibling(node)
        if RBTreeCase3(node, sib):
            """
            Color sibling red and call removal preparation function on parent
            """
            return
        if RBTreeCase4(node, sib):
            """
            Color parent black and sibling red
            """
            return
        if RBTreeCase5(node, sib):
            """
            Color sibling red and sibling's left child black. Rotate right at sibling
            """
            sib = self.get_sibling(node)
        if RBTreeCase6(node, sib):
            """
            Color sibling red and sibling's right child black. Rotate left at sibling
            """
            sib = self.get_sibling(node)
        sib.is_red = node.parent.is_red
        node.parent.is_red = False#Reset to balck
        if node.parent.left == node:
            sib.right.is_red = False
            self.left_rotate(node.parent)
        else:
            sib.left.is_red = False
            self.right_rotate(node.parent)

##################### Insertion and Removal #########################

    def insert(self, node: Node, val: Generic[T]) -> None:
        """
        Inserts an RBnode object to the subtree rooted at node with value val.
        Should a node with value val already exist in the tree, do nothing.
        Time Complexity: O(log(n)), Space Complexity: O(1)
        """
        def insertionSupplem(node: Node, val: Generic[T]) -> Node:
            """
            Inner Function Recursively to wrap the insert function
            """
            if not node:
                return Node(val, True)
            if node.value < val:
                node.right = insertionSupplem(node.right, val)
                node.right.parent = node
            elif node.value > val:
                node.left = insertionSupplem(node.left, val)
                node.left.parent = node
            else:
                self.size -= 1
            return node

        if not self.root:
            self.root = Node(val, False)
            self.size += 1
            return
        insertionSupplem(node, val)
        self.insertion_repair(self.search(node, val))
        self.size = self.size + 1

    def remove(self, node: Node, val: Generic[T]) -> None:
        """
        Removes node with value val from the subtree rooted at node. If no such node exists, do nothing.
        Time Complexity: O(log(n)), Space Complexity: O(1)
        """
        def deletion(node: Node, val: Generic[T]):
            """
            Inner Function Recursively to wrap the remove function
            """
            if node.right:
                if node.left:
                    node.value = removeSupplem(node).value
                    deletion(removeSupplem(node), val)
                    return
            if not node.is_red:
                self.prepare_removal(node)
            self.size = self.size - 1
            #Case#1 Must before Case#2 First Check all then part
            #Case#1 Both of them empty Reached the Last
            if not node.right and not node.left:
                if node.parent and node.parent.right and node.value == node.parent.right.value:
                    node.parent.right = None
                elif node.parent and node.parent.left and node.value == node.parent.left.value:
                    node.parent.left = None
                else:
                    self.root = None
                return
            #Case#2 One of then empty Go To Next Not Empty
            if not node.left or not node.right:
                if node.left:
                    next_child = node.left #Go To Left
                else:
                    next_child = node.right #Go To Right
                if node.parent:
                    if node.parent.right and node.value == node.parent.right.value:
                        node.parent.right = next_child
                    else:
                        node.parent.left = next_child
                else:
                    self.root = next_child
                    self.root.is_red = False
                next_child.parent = node.parent
                return
        def removeSupplem(node: Node) -> Node:
            """
            Recursively update the node to right as inner function.
            """
            node = node.left
            if not node.right:
                return node
            while True:
                if node.right is None:
                    return node
                node = node.right

        node = self.search(node, val)
        if not node:
            return
        deletion(node, val) #Wrao inner function
        return
