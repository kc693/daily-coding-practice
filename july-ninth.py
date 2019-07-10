""" This problem was asked by LinkedIn.

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key 
in the left child must be less than or equal to the root and the key in the right child must be greater than or equal to the root. """

def validTree(root, tree_min, tree_max):
    # root is a node and tree_min/tree_max are integer values

    if root is None:
        return true

    if tree_min > root.val or tree_max < root.val:
        return False
    else:
        left = True
        right = True
        if root.left is not None:
            left = validTree(root.left,tree_min,root.val)
        if root.right is not None:
            right = validTree(root.right,root.val,tree_max)

        return left and right

### still unsure how this works
