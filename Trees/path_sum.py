class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def path_sum(root, k):
    
    if root is None:
        return False
    result = [False]
    
    def helper(node, target):
        if node is None:
            return 
        
        if node.left is None and node.right is None:
            if target == node.value:
                result[0] = True
            return 
        
        if node.left is not None:
            helper(node.left, target-node.value)
        if node.right is not None:
            helper(node.right, target-node.value)
            
    helper(root, k)
    return result[0]
