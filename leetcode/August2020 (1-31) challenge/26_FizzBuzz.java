import java.util.*;

class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> list1 = new ArrayList();  

        for(int i=1; i<n+1; i++)
        {
            if(i%15 == 0) list1.add("FizzBuzz");
            else if(i%5 == 0) list1.add("Buzz");
            else if(i%3 == 0) list1.add("Fizz");
            else list1.add(Integer.toString(i));
        }
        return list1;
    }
}

class Main
{
    public static void main(String[] args)
    {
        Solution s = new Solution();
        // System.out.println("search: " + s.fizzBuzz(15));
        List<String> z = s.fizzBuzz(15);
        for(String x:z) System.out.println(x);
    }
}
