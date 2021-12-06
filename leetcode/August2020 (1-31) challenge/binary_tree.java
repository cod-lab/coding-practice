class Node
{
    int root;                           // root at first
    Node left, right;

    public Node(int root)
    {
        this.root = root;
    }

    // public void insert(Node left, Node right, int x)           // x = no. to be inserted in tree 
    public void insert(int x)           // x = no. to be inserted in tree 
    {
        if(x<=root)
        {
            if(left==null)                      // if left is null
                left = new Node(x);             // then in initialize left
            else
                // left.insert(left, right, x);
                left.insert(x);
        }
        else
        {
            if(right==null)
                right = new Node(x);
            else
                // right.insert(left, right, x);
                right.insert(x);
        }
    }

    // public boolean contains(Node left, Node right, int x)
    public boolean contains(int x)
    {
        if(x==root)
            return true;
        else if(x<root)
        {
            if(left==null)
                return false;
            else
                // return left.contains(left, right, x);
                return left.contains(x);
        }
        else
        {
            if(right==null)
                return false;
            else
                // return right.contains(left, right, x);
                return right.contains(x);
        }
    }

    // public void inOrder(Node left, Node right)
    public void inOrder()
    {
        if(left!=null)                  // first check left side
            // left.inOrder(left, right);
            left.inOrder();

        System.out.println(root);       // prints current nodes parent

        if(right!=null)                     // then chk right of each current node
            // right.inOrder(left, right);
            right.inOrder();
    }
}

class Main
{
    public static void main(String[] args)
    {
        // int root;                           // root at first
        // Node left, right;
        Node n = new Node(1);

        int[] list = {1,2,3,4,5,6,7};
        // int[] list = {3,5,6,2,4,7};
        for(int i=0; i<list.length; i++)
        {
            // left.insert(left, right, list[i]);
            // right.insert(left, right, list[i]);

            n.insert(list[i]);
        }

        n.inOrder();
    }

}