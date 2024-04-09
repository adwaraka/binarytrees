from binaryTree import (
    Node,
    insert,
    inorder,
    preorder,
    isIdentical,
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


if __name__ == "__main__":
    main()