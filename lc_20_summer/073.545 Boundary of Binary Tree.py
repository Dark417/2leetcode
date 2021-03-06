"""
073.545	Boundary of Binary Tree
二叉树的边界

给定一棵二叉树，以逆时针顺序从根开始返回其边界。边界按顺序包括左边界、叶子结点和右边界而不包括重复的结点。 
(结点的值可能重复)

左边界的定义是从根到最左侧结点的路径。右边界的定义是从根到最右侧结点的路径。若根没有左子树或右子树，
则根自身就是左边界或右边界。注意该定义只对输入的二叉树有效，而对子树无效。

最左侧结点的定义是：在左子树存在时总是优先访问，如果不存在左子树则访问右子树。重复以上操作，
首先抵达的结点就是最左侧结点。

最右侧结点的定义方式相同，只是将左替换成右。

示例 1

输入:
  1
   \
    2
   / \
  3   4

输出:
[1, 3, 4, 2]

解析:
根不存在左子树，故根自身即为左边界。
叶子结点是3和4。
右边界是1，2，4。注意逆时针顺序输出需要你输出时调整右边界顺序。
以逆时针顺序无重复地排列边界，得到答案[1,3,4,2]。
 

示例 2

输入:
    ____1_____
   /          \
  2            3
 / \          / 
4   5        6   
   / \      / \
  7   8    9  10  
       
输出:
[1,2,4,7,8,9,10,6,3]

解析:
左边界是结点1,2,4。(根据定义，4是最左侧结点)
叶子结点是结点4,7,8,9,10。
右边界是结点1,3,6,10。(10是最右侧结点)
以逆时针顺序无重复地排列边界，得到答案 [1,2,4,7,8,9,10,6,3]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/boundary-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



"""


def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:



	
def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
    left_b, right_b, leaves = [], [], []
    def get_left_boundary(node):
        if not node: return
        left_b.append(node.val)
        if node.left: get_left_boundary(node.left)
        else: get_left_boundary(node.right)

    def get_right_boundary(node):
        if not node: return
        right_b.append(node.val)
        if node.right: get_right_boundary(node.right)
        else: get_right_boundary(node.left)
    
    def get_leaves(node):
        if not node: return None
        if not node.left and not node.right:
            leaves.append(node.val)
            return
        get_leaves(node.left)
        get_leaves(node.right)

    if root == None: return []
    if not root.left and not root.right: return [root.val]


































