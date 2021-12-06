// import javax.swing.tree.TreeNode;

public class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution
{
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        
        List<List<Integer>> l = new List<List<Integer>>();
    }
}

class Main
{
    public static void main(String[] args)
    {
        TreeNode root = new TreeNode();
        Solution s = new Solution();

        System.out.println("list: " + s.verticalTraversal(root));
    }
}