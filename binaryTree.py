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
    if not root:
        return 0

    if not root.left and not root.right:
        return 1

    left = minDepth(root.left) if root.left else float('inf')
    right = minDepth(root.right) if root.right else float('inf')
    return min(left, right) + 1


def maxDepth(root):
    if not root:
        return 0

    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return max(left_depth, right_depth) + 1
