from binaryTree import (
    Node,
    insert,
    inorder,
    preorder,
    isIdentical,
    isSymmetricTree,
    minDepth,
    maxDepth,
    diameterOfBinaryTree,
    printRightSide,
)

def main():
    import random
    L = range(100)
    amount = 5
    inputArr = [random.choice(L) for _ in range(amount)]
    print(inputArr)
    root = Node(inputArr[0])
    for val in inputArr[1:]:
        insert(root, Node(val))
    inorder(root)
    print()
    preorder(root)
    dupArr = inputArr
    print()
    dupRoot = Node(dupArr[0])
    for val in dupArr[1:]:
        insert(dupRoot, Node(val))    
    print(isIdentical(root, dupRoot))
    # TODO; better testing for symmetry
    print(isSymmetricTree(root))
    print(minDepth(root))
    print(maxDepth(root))
    print()
    print("rootD")
    rootD = Node(1)
    rootD.left = Node(2)
    rootD.right = Node(3)
    rootD.left.left = Node(4)
    rootD.left.right = Node(5)
    rootD.left.left.left = Node(6)
    #
    #            1
    #          /   \
    #        2       3
    #       /  \
    #     4     5
    #    /
    #  6
    #
    # inorder(rootD)
    print(f"Diameter: {diameterOfBinaryTree(rootD)}")
    printRightSide(rootD)


if __name__ == "__main__":
    main()