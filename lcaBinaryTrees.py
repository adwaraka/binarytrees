# LCA for a Binary Tree; not a BST
class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def leastCommonAncestor(root, lNode, rNode):
    if root is None:
        return None

    if root.data == lNode.data or root.data == rNode.data:
        return root.data
    else:
        lcaLeft = leastCommonAncestor(root.left, lNode, rNode)
        lcaRight = leastCommonAncestor(root.right, lNode, rNode)

        # success because the following means the left node is
        # present in left subtree and right in right subtree
        if lcaLeft and lcaRight:
            return root.data

        if lcaLeft:
        	# means only the left subtree will have the LCA
            return lcaLeft
        if lcaRight:
        	# means only the right subtree will have the LCA
            return lcaRight


# standalone main
def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.left = Node(8)

    lNode = root.right.right
    rNode = root.right.left.left
    print(leastCommonAncestor(root, lNode, rNode))


if __name__ == "__main__":
    main()