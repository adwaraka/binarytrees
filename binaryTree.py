from typing import Optional

class Node():
    def __init__(self, data=None):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            # right node does not exist
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            # left node does not exist
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


# inorder traversal
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


# preorder traversal
def preorder(root):
    if root is not None:
        # push to bottom for postorder
        print(root.data)
        preorder(root.left)
        preorder(root.right)


# count number of leaves
def countLeaves(root):
    if root is None:
        return 0
    # leaves will have no children
    elif root.left is None and root.right is None:
        return 1
    return countLeaves(root.left) + countLeaves(root.right)


# check if BTs are identical
def isIdentical(x, y):
    # x and y nodes do not exist
    if x is None and y is None:
        return True
    return (x is not None and y is not None) and \
           (x.data == y.data) and \
           isIdentical(x.left, y.left) and isIdentical(x.right, y.right)


# check if BT is symmetric
def isSymmetricTree(root):
    # tree itself does not exist
    if root is None:
        return True
    return isSymmetric(root.left, root.right)


def isSymmetric(x, y):
    # x and y nodes do not exist
    if x is None and y is None:
        return True
    return (x is not None and y is not None) and \
           isSymmetric(x.left, y.right) and isSymmetric(x.right, y.left)


def minDepth(root):
    # called on root = NULL
    if root is None:
        return 0
     
    # Base Case : Leaf node.This accounts for height = 1
    if root.left is None and root.right is None:
        return 1
     
    # If left subtree is Null, recur for right subtree
    if root.left is None:
        return minDepth(root.right)+1
     
    # If right subtree is Null, recur for left subtree
    if root.right is None:
        return minDepth(root.left) +1
     
    return min(minDepth(root.left), minDepth(root.right))+1


def maxDepth(root):
    if not root:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return max(left_depth, right_depth) + 1


def diameterOfBinaryTree(root):
    def dfs(node, maxDiameter):
        if node is None:
            return 0
        leftDepth = dfs(node.left, maxDiameter)
        rightDepth = dfs(node.right, maxDiameter)
        # is the new diameter greater than the old one?
        maxDiameter = max(maxDiameter, leftDepth + rightDepth)
        # return the diameter i.e left depth + right depth
        return 1 + max(leftDepth, rightDepth)
    return dfs(root, 0)


def printRightSide(root):
    if root:
        queue = [root]
        while queue:
            n = len(queue)
            while n > 0:
                n-=1
                # pick the first element from queue
                temp = queue.pop(0)
                if n == 0:
                    print(temp.data)
                if temp.left:
                    # if right does not exist, you still need to
                    # # see the left and or it's children
                    queue.append(temp.left)
                if temp.right:
                    # the right node is added
                    queue.append(temp.right)
    else:
        print("None")
 

# reference: https://www.geeksforgeeks.org/flip-binary-tree/
'''
        2 <- root
       / \
      4   5
    root.left.left = root.right

        2
       / \
      4   5
     /
    5
    root.left.right = root
    4 points to 2

        4
       / \
      5   2
'''
def flipBinaryTree(root):
    if root is None:
        return root  # it returns the original root
    if root.left is None and root.right is None:
        return root  # same as above
    flippedRoot = flipBinaryTree(root.left)
    root.left.left = root.right
    root.left.right = root
    root.left = root.right = None
    return flippedRoot


def printLevelOrder(root):
    if root is None:
        return None
    queue = []
    queue.append(root)
    while queue:
        nodeCount = len(queue)
        while nodeCount > 0:
            node = queue.pop(0)
            print(node.data, end=" ")
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            nodeCount -= 1
        print()
