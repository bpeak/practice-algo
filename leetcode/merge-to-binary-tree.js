var mergeTrees = function(t1, t2) {
    if(!t1) {
        return t2
    }
    if(!t2){
        return t1
    }
    const t = new TreeNode(t1.val + t2.val)
    t.left = mergeTrees(t1.left, t2.left)
    t.right = mergeTrees(t1.right, t2.right)
    return t
};