from typing import Optional, List
from src.datastructures.tree_node import TreeNode


'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.


Example 1:

Input: root = [1,null,2,3]

Output: [1,3,2]

Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,2,6,5,7,1,3,9,8]

Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]
'''


class BinaryTreeInorderTraversal:
    def inorder__traversal(self, root: Optional[TreeNode]) -> List[int]:
        visited_nodes = set()
        traversal_stack = []
        inorder_list = []
        if type(root) is not type(None):
            traversal_stack.append(root)
            while len(traversal_stack) != 0:
                node = traversal_stack.pop()
                visited_nodes.add(node)
                if node.left is not None and node.left not in visited_nodes:
                    traversal_stack.append(node)
                    traversal_stack.append(node.left)
                elif node.right is not None and node.right not in visited_nodes:
                    inorder_list.append(node.val)
                    traversal_stack.append(node.right)
                else:
                    inorder_list.append(node.val)
        return inorder_list