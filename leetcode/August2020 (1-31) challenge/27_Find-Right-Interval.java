import java.util.*;

class Solution {
    public int[] findRightInterval(int[][] intervals) {
        
        int[] result = new int[intervals.length];
        // List<Integer> l = new ArrayList<>();
        int[][] a = new int[intervals.length*3][intervals.length*3];
        // int[] b = new int[intervals.length];

        for(int i=0; i<intervals.length; i++)
        {
            for(int j=0; j<intervals.length; j++)
            {
                int k=0;
                a[k][0] = j;
                if(intervals[i][1] <= intervals[j][0])
                {
                    a[k][1] = intervals[j][0];
                    // result[i] = j;
                }
                else
                {
                    // a[j][0] = j;
                    a[k][1] = -1;
                    // result[i] = j;
                }
                k++;   //  result[i] = -1;
            }
            //  result[i] = Collections.min(Arrays.asList(a[i][1]));
        }
        for (int[] row : a) 
            System.out.println("a: " + Arrays.toString(row));

        return result;
    }
}

class Main
{
    public static void main(String[] args)
    {
        int[][] intervals = { {3,4}, {4,5}, {5,6}, {2,7} };
        Solution s = new Solution();
        
        System.out.println("list: " + Arrays.toString(s.findRightInterval(intervals)));
        // for(String x:z) System.out.println(x);
    }
}
