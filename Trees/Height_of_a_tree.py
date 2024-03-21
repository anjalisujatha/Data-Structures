
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def find_height(root):
  
    if root is None:
        return 0
        
    def helper(node):
        if not node.children:  
            return 0
        
        max_child_height = 0
        for child in node.children:
            child_height = helper(child)
            max_child_height = max(max_child_height, child_height)
            
        return 1 + max_child_height
        
    return helper(root)
    