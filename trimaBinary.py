#Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). 
#You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if root.left is not None:
            #return trimBST(self, root.left, L, R)
            return self.trimBST(root.left, L, R)
        if root.val > R or root.val < L:
            root = self.removeNode(root)
        if root.right is not None: 
            return self.trimBST(root.right, L, R)


    def removeNode(self, node:TreeNode) -> TreeNode:

        if not(node.left or node.right): return None

        if node.left:
            temp = node.left
            temp.right = node.right
            if node.right: node.right.left = temp
        elif node.right:
            temp = node.right
            temp.left = None
    
        return temp


    def insertNode(self, node:TreeNode, val: int) -> TreeNode:
        if node.left is None: 
            node.left = TreeNode(val)
            return node.left
        elif node.right is None:
            node.right = TreeNode(val)
            return node.right
        
    def printTree(self, node:TreeNode):
        if node.left:
            self.printTree( node.left)
        print(node.val)
        if node.right:
            self.printTree(node.right)


myroot = TreeNode(1)
obj = Solution()

param_1 = obj.insertNode(myroot, 0)
param_1 = obj.insertNode(myroot, 2)
obj.printTree(myroot)
param_2 = obj.trimBST(myroot, 1, 2)
obj.printTree(myroot)




        


                
        