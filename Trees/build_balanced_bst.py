class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_balanced_bst(a):
    
    def helper(A, start, end):
        if start > end:
            return None
        if start == end:
            return BinaryTreeNode(A[start])
        
        mid = start + (end-start)//2
        subroot = BinaryTreeNode(A[mid])
        subroot.left = helper(A, start, mid-1)
        subroot.right = helper(A, mid+1, end)
        return subroot
        
    return helper(a, 0, len(a)-1)
