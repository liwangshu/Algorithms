# Binary Search Tree
# Methods: search, insert, preOrder, inOrder, postOrder

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# insert: recursive
def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# insert: non-recursive
def insert2(root, key):
    if not root:
        return TreeNode(key)
    pre = None
    cur = root
    while cur:
        pre = cur
        if key < cur.val:
            cur = cur.left
        else:
            cur = cur.right
    cur = TreeNode(key)
    if key < pre.val:
        pre.left = cur
    else:
        pre.right = cur
    return root

# search: recursive
def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

# search: non-recursive
def search2(root, key):
    while root:
        if root.val == key:
            return root
        if root.val < key:
            root = root.right
        else:
            root = root.left
    return None

# pre-order: recursive
def preOrder(root):
    if not root:
        return
    print(root.val, end = ' ')
    preOrder(root.left)
    preOrder(root.right)

# pre-order: non-recursive
def preOrder2(root):
    if root is None:
        return
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        print(node.val, end = ' ')
        if node.right:  # right is pushed first so that left is processed first
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
            
# in-order: recursive
def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.val, end = ' ')
    inOrder(root.right)

# in-order: non-recursive
def inOrder2(root):
    stack = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        print(cur.val, end = ' ')
        cur = cur.right

# post-order: recursive
def postOrder(root):
    if not root:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.val, end = ' ')

# post-order: non-recursive: only one stack
def postOrder2(root):
    if not root:
        return
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        if node:
            stack.append(node)
            stack.append(None)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        else:
            node = stack.pop()
            print(node.val, end = ' ')

# post-order: nonrecursive: one stack, one set
def postOrder3(root):
    stack = []
    cur = root
    visited = set()
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        node = stack[-1]
        if node not in visited:
            visited.add(node)
            cur = node.right
        else:
            print(node.val, end = ' ')
            stack.pop()
    
# post-order: non-recursive: two stacks
def postOrder4(root):
    if root is None:
        return
    s1 = []
    s2 = []
    s1.append(root)
    while s1:
        node = s1.pop()
        s2.append(node)
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
    while s2:
        print(s2.pop().val, end = ' ')

# Create following BST
#       4
#     /  \
#    1    6   
#   / \  / \
#  0  2 5  7
#      \
#      3

t = None
t = insert(t, 4)
t = insert2(t, 1)
t = insert(t, 2)
t = insert2(t, 6)
t = insert(t, 0)
t = insert2(t, 5)
t = insert(t, 7)
t = insert2(t, 3)

print(search(t, 3).val)
print(search(t, 9))
print(search2(t, 5).val)
preOrder(t)
print()
preOrder2(t)
print()
inOrder(t)
print()
inOrder2(t)
print()
postOrder(t)
print()
postOrder2(t)
print()
postOrder3(t)
print()
postOrder4(t)