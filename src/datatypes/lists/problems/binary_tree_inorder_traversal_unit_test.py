import unittest
from typing import Optional

from binary_tree_inorder_traversal import BinaryTreeInorderTraversal
from src.datastructures.tree_node import TreeNode

class MyTestCase(unittest.TestCase):

    testEnv = BinaryTreeInorderTraversal()

    def test_empty_tree(self):
        self.assertEqual([], self.testEnv.inorder__traversal(None))

    def test_single_tree(self):
        tree_node = TreeNode(1)
        self.assertEqual([1], self.testEnv.inorder__traversal(tree_node))

    def test_three_tree(self):
        root_node = TreeNode(1)
        node_ptr = root_node
        node_ptr.right = TreeNode(2)
        node_ptr = node_ptr.right
        node_ptr.left = TreeNode(3)
        self.assertEqual([1,3,2], self.testEnv.inorder__traversal(root_node))

    def test_large_tree(self):
        root_node = TreeNode(1)
        node_ptr = root_node
        node_ptr.left = TreeNode(2)
        node_ptr.right = TreeNode(3)
        node_ptr = node_ptr.left
        node_ptr.left = TreeNode(4)
        node_ptr.right = TreeNode(5)
        node_ptr = node_ptr.right
        node_ptr.left = TreeNode(6)
        node_ptr.right = TreeNode(7)
        node_ptr = root_node.right
        node_ptr.right = TreeNode(8)
        node_ptr = node_ptr.right
        node_ptr.left = TreeNode(9)
        self.assertEqual([4,2,6,5,7,1,3,9,8], self.testEnv.inorder__traversal(root_node))

if __name__ == '__main__':
    unittest.main()
