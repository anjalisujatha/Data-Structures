class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_binary_search_tree(preorder):
   
    inorder = sorted(preorder)
    hmap = {}
    for i in range(len(inorder)):
        hmap[inorder[i]] = i
        
    def helper(A1, start1, end1, A2, start2, end2):
        if start1 > end1:
            return None
        if start1 == end1:
            return BinaryTreeNode(A1[start1])
            
        rootval = A1[start1]
        rootindex = hmap[rootval]
        numleft = rootindex -start2
        numright = end2-rootindex
        subtreeroot = BinaryTreeNode(A1[start1])
        subtreeroot.left = helper(A1, start1+1, start1+numleft, A2, start2, start2+numleft-1)
        subtreeroot.right = helper(A1, start1+numleft+1, start1+numleft+numright, A2, rootindex+1, rootindex+numright)
        return subtreeroot
    return helper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)
