# Project 3: Red Black Trees

**Due: Thursday, October 22nd @ 8:00pm**

_This is not a team project, do not copy someone else’s work._

## Assignment Overview

### Red/Black Tree

![500px-Red-black_tree_example.svg.png](https://s3.amazonaws.com/mimirplatform.production/files/1f173bcd-00a3-4581-88f0-f82d243d789f/500px-Red-black_tree_example.svg.png)

A Red Black Tree is a type of self-balancing binary search tree (BST). A BST is a binary tree with the property that given a node contained therein, its left and right children store values less and greater than it respectively. This allows for, on average, logarithmic time complexity of searches. BSTs can, as has been discussed in class, become unbalanced when subject to certain sequences of insertions or removals. A self balancing BST seeks to remedy this issue by ensuring that given a node, its left and right branches are of relatively equal size. A Red Black tree ensures this balance by assigning a color (red or black) to each node and applying rules to the ways in which these colors are distributed. These rules are as follows:

1.  Each node must be either Red or Black.
2.  The root of the tree must always be Black.
3.  A Red node must always have a Black parent node, and a Black child node (as shown above, null nodes are assumed to be Black).
4.  Every path from the root of the tree to a null pointer must pass through the <span style="text-decoration: underline;">same number</span> of black nodes.

The method by which these rules maintain balance is best discussed in further depth than feasible in a project description, and can be readily found online. A few links, though, may be helpful.

[Here is a visualization tool](https://www.cs.usfca.edu/~galles/visualization/RedBlack.html) which is very useful for testing insertions and removals. We used this while developing the project.

[Information on static methods in python.](https://pythonbasics.org/static-method/)

[Information on python generators and yield statements.](https://realpython.com/introduction-to-python-generators/#building-generators-with-generator-expressions) (This is more than you need to use for this project.)

[Here is some information](https://www.geeksforgeeks.org/red-black-tree-vs-avl-tree/) on the differences between Red Black trees and AVL trees, which this project was based on in previous semesters.

## Assignment Notes

IMPORTANT: Don't create new objects without good reason. Never in the course of this project should one create a new tree, and new nodes should only be created within **insert().** Doing so in other situations is very likey to violate complexity requirements, and never necessary.

*   Remember to write docstrings. Project 1 provides examples of how they should be written. Docstrings should include a description of the function they pertain to, its parameters, and its return type.
*   An **RBtree **is strictly typed, and will not contain mismatched types. However, the structure should be type agnostic and able to contain any standard type.
*   Several of the method implemented are **static methods** - the reason for this is that while they are members of the **RBtree **class, they act only on the **RBnode** class, and are not called on an **RBtree**. I.e. rather than calling on `self` (an **RBtree** instance) with `self.get_uncle(node)`, one would call the function `RBtree.get_uncle(node)`.
*   The methods below are given in a suggested logical order of implementation.
*   **IT IS HIGHLY RECOMMENDED YOU REFER TO THE SECTIONS OF ZYBOOKS RELEVANT TO THE PROJECT BEFORE AND DURING IMPLEMENTATION!**
*   **remove()** and **prepare_removal()** are large functions. Consider ways in which one may divide it into multiple functions (hint: look at zybooks).
*   As the above note should indicate, feel free to implement helper functions as necessary- as long as they obey time and space complexity requirements.
*   For traversals, use of recursion is highly recommended.
*   This project will **not have an application problem** due to the complexity and difficulty of implemeting Red Black trees. With that said, <span style="text-decoration: underline;">_make sure you start this project early._</span>
*   **Types:**
    *   **T**: Generic Type
    *   **RBnode**: Described below

## Assignment Specifications

### class RBnode: 

This class describes the nodes contained in an **RBtree**.

**_DO NOT MODIFY this class_**

*   **Attributes**
    *   **value**: Value contained in a node. Is also used as a key insertion, removal, and other pertinent operations.
    *   **is_red:** Boolean identifier for node color (if it is not red, it is black)
    *   **parent:** Parent of the node
    *   **left:** Left child of the node
    *   **right:** Right child of the node

*   **__init__**(self, value, is_red=True, parent=None, left=None, right=None)  

    *   **val**: **T **
    *   **is_red**: **bool**
    *   **parent**: **RBnode**
    *   **left**: **RBnode**
    *   **right**: **RBnode**
    *   Instantiates an **RBnode**, assigning its member variables.
    *   return: **None**
    *   _Time Complexity: O(1)_
*   **__eq__**(self, other)
    *   **other**: **RBnode**
    *   Assesses equality of data contained in a node, checking both **value** and **is_red**
    *   return: **bool**
    *   _Time Complexity: O(1)_
*   **__str__**(self)
    *   Representation of **val** and **is_red** as a string
    *   return: **str**
    *   _Time Complexity: O(1)_
*   **__repr__**(self)
    *   Representation as a string utilizing **__str__**
    *   return: **str**
    *   _Time Complexity: O(1)_
*   **subtree_size**(self)
    *   Size of a subtree rooted at _self_
    *   return: **int**
    *   _Time Complexity: O(n)_
*   **subtree_size**(self)
    *   Height of a subtree rooted at _self_
    *   return: **int**
    *   _Time Complexity: O(n)_
*   **subtree_red_black_property**(self)
    *   Determines whether the subtree rooted at _self_ adheres to Red Black properties
    *   return: **bool**
    *   _Time Complexity: O(n)_

### class RBtree: 

**_DO NOT MODIFY the following attributes/functions_**

*   **Attributes**
    *   **root**: root of an **RBtree**, of type **RBnode**
    *   **size**: number of nodes contained in the tree
*   **__init__**(self, root=None)
    *   **root**: **RBnode**
    *   Instantiates an **RBtree**, creating a deepcopy of the subtree rooted at a provided node. This provided node defaults to **None**.
    *   Size is assigned based on the described subtree.
    *   _Time Complexity: O(n) -_ where _n _is the size of the rooted subtree provided
*   **__eq__**(self, other)
    *   **other**: **RBtree**
    *   Determines equality between **RBtree** instances.
    *   return: **bool**
    *   _Time Complexity: O(min(N, M)) --> M is size of other  _
*   **__str__**(self)
    *   Represents the **RBtree** as a string, for use in debugging
    *   return: **str**
    *   _Time Complexity: O(N)_

*   **__repr__**(self)
    *   Represents the list as a string utilizing **__str__**
    *   return: **str**
    *   _Time Complexity: O(N)_

**_IMPLEMENT the following functions_**

*   **set_child**(parent, child, is_left) **--> static method**
    *   **parent**: **RBnode**
    *   **child**: **RBnode**
    *   **is_left**: **bool**
    *   Sets the childparameter of _parent _to _child_. Which child is determined by the identifier _is_left. _The parent parameter of the new child node should be updated as required.
    *   return: **None**
    *   _Time Complexity: O(1), Space Complexity: O(1)_
*   **replace_child**(parent, current_child, new_child) **--> static method**
    *   **parent**: **RBnode**
    *   **current_child**: **RBnode**
    *   **new_child**: **RBnode**
    *   Replaces **parent**'s child **current_child** with **new_child**.
    *   return: **None**
    *   _Time Complexity: O(1), Space Complexity: O(1)_
*   **get_sibling**(node) **--> static method**

*   *   **node**: **RBnode**
    *   Given a node, returns the other child of that node's parent, or **None **should no parent exist.
    *   _Time Complexity: O(1), Space Complexity: O(1)_
*   **get_uncle**(node) **--> static method**
    *   **node**: **RBnode**
    *   Given a node, returns the sibling of that node's parent, or **None **should no such node exist.
    *   _Time Complexity: O(1), Space Complexity: O(1)_
*   **get_grandparent**(node) **--> static method**
    *   **node**: **RBnode**
    *   Given a node, returns the parent of that node's parent, or **None **should no such node exist.
    *   _Time Complexity: O(1), Space Complexity: O(1)_
*   **left_rotate**(self, node)
    *   **node**: **RBnode**
    *   Performs a left tree rotation on the subtree rooted at _node_.
    *   return: **None**
    *   _Time Complexity: O(1), Space Complexity: O(1)_
*   **right_rotate**(self, node)
    *   **node**: **RBnode**
    *   Performs a right tree rotation on the subtree rooted at _node._
    *   return: **None**
    *   _Time Complexity: O(1), Space Complexity: O(1)_
*   **insertion_repair**(self, node)
    *   **node**: **RBnode**
    *   This method is not tested explicitly, but should be called after insertion on the node which was inserted, and should rebalance the tree by ensuring adherance to Red/Black properties.
    *   It is highly recommended you utilize recursion.
    *   return: **None**
    *   _Time Complexity: O(log(n)), Space Complexity: O(1)_
*   **prepare_removal**(self, node)
    *   **node**: **RBnode**
    *   This method is not tested explicitly, but should be called prior to removal, on a node that is to be removed. It should ensure balance is maintained after the removal.
    *   return: **None**
    *   _Time Complexity: O(log(n)), Space Complexity: O(1)_
*   **insert**(self, node, val)
    *   **node: RBnode**
    *   **val: Type T**
    *   Inserts an **RBnode **object to the subtree rooted at _node_ with value _val_.
    *   Should a node with value _val_ already exist in the tree, do nothing.
    *   It is _highly recommended _you implement this function recursively. To do so non-recursively will be significantly harder, and we won't assist you in doing so in the helproom or on piazza.
    *   return: **None**
    *   _Time Complexity: O(log(n)), Space Complexity: O(1)_
*   **search**(self, node, val)
    *   **node: RBnode**
    *   **val: Type T**
    *   Searches the subtree rooted at _node_ for a node containing value _val. _If such a node exists, return that node- otherwise return the node which would be parent to a node with value _val_ should such a node be inserted.
    *   This is probably best to implement recursively, but not required.
    *   _Time Complexity: O(log(n)), Space Complexity: O(1)_
*   **min**(self, node)
    *   **node: RBnode**
    *   Returns the minimum value stored in the subtree rooted at _node_. (**None** if the subtree is empty).
    *   _Time Complexity: O(log(n)), Space Complexity: O(1)_
*   **max**(self, node)
    *   **node: RBnode**
    *   Returns the maximum value stored in a subtree rooted at _node_. (**None** if the subtree is empty).
    *   _Time Complexity: O(log(n)), Space Complexity: O(1)_
*   **inorder**(self, node)
    *   **node: RBnode**
    *   Returns a _generator_ object describing an inorder traversal of the subtree rooted at _node._
    *   Points will be deducted if the return of this function is not a generator object (hint: **yield **and **yield ****from**)
    *   _Time Complexity: O(n), Space Complexity: O(n)_
*   **preorder**(self, node)
    *   **node: RBnode**
    *   Returns a _generator_ object describing a preorder traversal of the subtree rooted at _node._
    *   Points will be deducted if the return of this function is not a generator object (hint: **yield **and **yield ****from**)
    *   _Time Complexity: O(n), Space Complexity: O(n)_
*   **postorder**(self, node)
    *   **node: RBnode**
    *   Returns a _generator _object describing a postorder traversal of the subtree rooted at _node._
    *   Points will be deducted if the return of this function is not a generator object (hint: **yield **and **yield ****from**)
    *   _TIme Complexity: O(n), Space Complexity: O(n)_
*   **bfs**(self, node)
    *   **node: RBnode**
    *   Returns a _generator _object describing a breadth first traversal of the subtree rooted at _node_.
    *   Hint: the _queue _class has been imported already, feel free to use it.
    *   Points will be deducted if the return of this function is not a generator object (hint: **yield **and **yield ****from**)
    *   _Time Complexity: O(n), Space Complexity: O(n)_
*   **remove**(self, node, val)
    *   **node: RBnode**
    *   **val: Type T**
    *   Removes node with value _val _from the subtree rooted at _node_. If no such node exists, do nothing.
    *   If the node to be removed is an internal node with two children, swap its value with that of the maximum of its left subtree, then remove the node its value was swapped to.
    *   Using **search() **might be a good idea.
    *   This function is complicated and hard, don't be afraid to ask for help. We strongly recommend referring to zybooks.
    *   Note this function uses inorder traversals for testing, so your tests will not pass if the in order traversal function is not completed.
    *   return: **None**
    *   _Time Complexity: O(log(n)), Space Complexity: O(1)_

## Submission

#### Deliverables

Be sure to upload the following deliverables in a .zip folder to Mimir by 8:00p Eastern Time on Thursday, 10/22/20.

    Project3.zip
        |— Project3/
            |— README.md       (for project feedback)
            |— __init__.py     (for proper Mimir testcase loading)
            |— RBtree.py       (contains your solution source code)        |— RBnode.py       (supports RBtree.py)

#### Grading

*   Tests (70)
    *   Tests: __/70
*   Manual (30)  

    *   Time Complexity: __/14
        *   set_child, replace_child, get_sibling, get_uncle, get_grandparent, min, max, search (0.5 each)
        *   inorder, preorder, postorder, bfs, left_rotate, right_rotate (1 each)
        *   insert, remove (2 each)
    *   Space Complexity: __/14
        *   set_child, replace_child, get_sibling, get_uncle, get_grandparent, min, max, search (0.5 each)
        *   inorder, preorder, postorder, bfs, left_rotate, right_rotate (1 each)
        *   insert, remove (2 each)
    *   README.md is _completely_ filled out with (1) Name, (2) Feedback, (3) Time to Completion and (4) Citations: __/2

Project designed by Andrew Haas and Ian Barber
