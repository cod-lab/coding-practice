import java.util.concurrent.ThreadLocalRandom;

class Solution
{
    int n;
    public int rand7()
    {
        n = ThreadLocalRandom.current().nextInt(1, 7 + 1);
        return n;
    }

    public int rand10(Solution s) {

        // int m;
        // Solution s = new Solution();
        int m = s.rand7();
        int i=0;
        // if (m*m)
        switch(i)
        {
            case 0:
                switch(m+m)
                {
                    case 2:
                        return m+m+8;   // 
                    case 4:
                        return m+m+6;
                    case 6:
                        return m+m+4;
                }
            case 1:
                switch(m+m)
                {
                    case 3:
                        return m+m+7;
                    case 5:
                        return m+m+5;
                    case 7:
                        return m+m+3;
                }
        }

        return s.rand7() + 10;
    }
}

class Main
{
    public static void main(String[] args)
    {
        // int[][] intervals = { {3,4}, {4,5}, {5,6}, {2,7} };
        Solution s = new Solution();
        
        // System.out.println("list: " + Arrays.toString(s.findRightInterval(intervals)));
        // for(String x:z) System.out.println(x);
        System.out.println("(1-10)no: " + s.rand10(s));
    }
}
