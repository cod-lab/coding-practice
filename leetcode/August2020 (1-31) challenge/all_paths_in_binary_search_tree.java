import java.util.*;

class TreeNode
{
    int x;
    TreeNode left, right;

    TreeNode(int x)
    {
        this.x = x;
    }

    public void insert(int y)           // creating tree
    {
        if(y<=x)
        {
            if(left == null) left = new TreeNode(y);
            else left.insert(y);
        }
        else
        {
            if(right == null) right = new TreeNode(y);
            else right.insert(y);
        }

        // System.out.println("left:" + y); // Integer.toString(y));
    }

    public void inOrder()               // printing tree nodes in Inorder
    {
        if(left != null) left.inOrder();

        System.out.println(x);

        if(right != null) right.inOrder();
    }

    // @Override
    // public String toString()
    // {
    //     return "x: " + x; // + "y: " + y;
    // }
    // Solution s = new Solution();
    // s.binaryTreePaths(root);
    
}

// class Building_tree
// {
//     TreeNode root;
    
//     public void insert(int y)
//     {
//         if(y<=tree.x)
//     }
// }

class Solution
{
    public List<String> binaryTreePaths(TreeNode root)
    {
        List<String> result = new ArrayList<String>();

        if(root == null) return result;         // if root is null means there's no tree
        // else
        String current_path = Integer.toString(root.x);     // adding root to 'current_path'

        if(root.left == null && root.right == null) return result;  // if left, right r null i.e. only 1 node i.e. root
        // else if
        if(root.left != null) dfs(root.left, current_path, result); // if left not null then call dfs(root.left)
        // else
        if(root.right != null) dfs(root.right, current_path, result);    // if right not null then call dfs(root.right)

        return result;
    }

    public void dfs(TreeNode node, String current_path, List<String> result)
    {
        current_path += "->" + node.x;

        if(node.left == null && node.right == null) 
        {
            result.add(current_path);
            return;
        }
        // else if
        if(node.left != null) dfs(node.left, current_path, result); // if left not null then call dfs(node.left)
        // else
        if(node.right != null) dfs(node.right, current_path, result);    // if right not null then call dfs(node.right)
    }
}

class Main
{
    public static void main(String[] args)
    {
        // int root;                           // root at first
        // Node left, right;
        // TreeNode root, n;
        TreeNode n = new TreeNode(1);
        // n.insert(root);

        // int[] list = {1,2,3,4,5,6,7};
        // int[] list = {3,5,6,2,4,7};
        // int[] list = {8, 4, 5, 2, 6, 7, 3, 1};
        // int[] list = {5,1,3,2};
        String[] list = {"10","5","-3","3","2","null","11","3","-2","null","1"};
        for(int i=0; i<list.length; i++)
        {
            // left.insert(left, right, list[i]);
            // right.insert(left, right, list[i]);
            if(list[i] != "null") n.insert(Integer.parseInt(list[i]));
        }
        n.inOrder();

        Solution s = new Solution();
        System.out.println(s.binaryTreePaths(n));
    }
}
