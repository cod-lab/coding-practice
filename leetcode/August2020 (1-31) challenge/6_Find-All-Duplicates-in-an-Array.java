import java.util.*;
// import java.util.stream.Collectors;
import java.lang.Math; 

class Solution
{
    public List<Integer> findDuplicates(int[] nums) {
        System.out.println("new nums: " + nums);

        /*
        // List<Integer> l = Arrays.asList(nums);
        
        List<Integer> l = Arrays.stream(nums).boxed().collect(Collectors.toList());
        Collections.sort(l);  
        System.out.println(l);

        // int[] temp;

        // if(l.get(l.size()-1) != l.get(l.size()-2))
        //     l.remove(l.size()-1);
        // System.out.println(l.size());
        // int i = 0;
        for(int i=0; i<l.size(); i++)
        // while(i<l.size())
        {
            // i++;
            int j=0;
            if(l.get(j) != l.get(j+1))
            {
                System.out.print("i: " + j + " [" + l.get(j) + ", " + l.get(j+1) + "] ");
                // System.out.println("i+1: " + l.get(i+1));
                l.remove(j--);
                // i--;
                System.out.println(l + " " + j);
            }
            // else
                j++;
        }
        */
    
        // Method 1     (high Time Complexity but passed all test cases)
        /*
        Arrays.sort(nums);

        List<Integer> l = new ArrayList<>();

        for(int i=0; i<nums.length-1; i++)
        {
            if(nums[i] == nums[i+1])
                l.add(nums[i]);
        }
        */

        // Method 2
        List<Integer> l = new ArrayList<>();

        for(int j=0; j<nums.length; j++)
        {
            if(nums[Math.abs(nums[j])-1] < 0)       // if no. already Z-
                l.add(Math.abs(nums[j]));           // add that no.'s index to l
            nums[Math.abs(nums[j])-1] *= -1;        // convert to Z- each no. by using other no. as index
        }

        System.out.println("new nums: " + nums);
        return l;
    }
}

class Main
{
    public static void main(String[] args)
    {
        int[] nums = {4,3,2,7,8,2,3,1};

        Solution s = new Solution();

        System.out.println("list: " + s.findDuplicates(nums));
    }
}
