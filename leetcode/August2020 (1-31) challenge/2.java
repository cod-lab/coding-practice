import java.util.*;

class MyHashSet {
    // MyHashSet m = new MyHashSet();
    // ArrayList<List<Integer> > hs;
    // int j = h.indexOf(key);
    // LinkedList<Integer> h; // = new ArrayList<>();
    // MyHashSet m = new MyHashSet();
    // int[] h1;
    List<Integer> h1;
    int n = 10;
    int i=-1;

    public MyHashSet() {
        // int[][] hs = new int[][];
        // ArrayList<ArrayList<Integer> > x = new ArrayList<ArrayList<Integer> >(); 
        // ArrayList<List<Integer> > listOfLists = new ArrayList<List<Integer> >(); 
        // h  = new LinkedList<>();

        // i = key % n;
        // for(int k=0; k<h1.length;)
        // {
            //     if(h1[k] == key) j=k;
            //     else k++;
            // }
        // h1 = new int[n];
        h1 = new ArrayList<>(n);
        h1.addAll(-1);
        System.out.println("hash(a): " + Arrays.toString(h1));
    }

    // public int index(int key)
    // {
    //     i = key % n;
    //     // j = h.indexOf(key);
    //     for(int k=0; k<h1.length;)
    //     {
    //         if(h1[k] == key) j=k;
    //         else k++;
    //     }
    //     return j;
    // }

    public void add(int key) {
        // if(h != full)
        // MyHashSet m = new MyHashSet(key);

        // for(int k=0; k<h1.length;)
        // {
        //     if(h1[k] == key) j=k;
        //     else k++;
        // }
        // if(j == -1)
        // {
        //     int i = key % n;
        //     // h.add(i,key); // [i] = key;
        //     System.out.println("i: " + i);
        //     System.out.println("key: " + key);
        //     h1[i] = key;
        // }

        for(int k=0; k<h1.length; k++)
            if(h1[k] == key) return;

        i = key % n;
            
        System.out.println("i: " + i);
        System.out.println("key: " + key);

        h1[i] = key;

        System.out.println("hash(a): " + Arrays.toString(h1));
    }

    public void remove(int key) {
        for(int k=0; k<h1.length; k++)
        {
            if(h1[k] == key)
            {
                i = key % n;
                h1[i] = -1;
                break;
            }
            // j=k;
        }
        System.out.println("hash(r): " + Arrays.toString(h1));
    }

    public boolean contains(int key) {
        // MyHashSet m = new MyHashSet(key);
        for(int k=0; k<h1.length; k++)
            if(h1[k] == key) return true;
        return false;

        // {
        //     if(h1[k] == key) return true;
        //     else k++;
        // }
        // if(j == -1) return false;
            
        // {
            //     // j=k;
                
            // }
            // k++;
        // }
        // if(j == -1) return false;
        // else return false;
    }
}

class Main
{
    public static void main(String[] args)
    {
        int key = 7;

        MyHashSet obj = new MyHashSet();

        // obj.index(key);

        obj.add(key);
        obj.remove(key);
        boolean param_3 = obj.contains(key);
        
        System.out.println("contains: " + param_3);
    }
}
