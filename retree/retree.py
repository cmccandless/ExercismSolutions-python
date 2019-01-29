def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError('traversal lengths must be equal')
    if not preorder:
        return {}
    root_index = inorder.index(preorder[0])
    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index + 1:]
    return {
        'v': preorder[0],
        'l': tree_from_traversals(
            [x for x in preorder if x in left_inorder],
            left_inorder
        ),
        'r': tree_from_traversals(
            [x for x in preorder if x in right_inorder],
            right_inorder
        )
    }
