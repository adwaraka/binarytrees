class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


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
                temp = queue.pop(0)
                if n == 0:
                    print(temp.data)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
    else:
        print("None")
 