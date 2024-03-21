class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def kth_smallest_element(root, k):
    
    result = []
    def inorder(root):
    
        if root is None:
            return 
        
        inorder(root.left)
        result.append(root.value)
        inorder(root.right)
    inorder(root)
    
    if k <= len(result):
        return result[k-1]
    else:
        return -1
    