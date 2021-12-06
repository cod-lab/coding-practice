class Solution {
    public boolean detectCapitalUse(String word) {
        int m = word.length();
        if(m>1)
        {
                // int[] x = new int[m];
            
                // for(int i=0; i<m; i++)
                // {
                //     if(Character.isUpperCase(word.charAt(i))) x[i] = 1;
                //     else x[i] = 0;
                // }
                // System.out.println(Arrays.toString(x));

            int no_of_caps = 0; //, no_of_zeros = 0;
            for(int i=1; i<m; i++)
            {
                if(Character.isUpperCase(word.charAt(i))) no_of_caps++;
                // else no_of_zeros++;
            }

            if(no_of_caps>0 && no_of_caps<m-1) return false;     // mix
            else
            {
                if(no_of_caps==m-1)
                {
                    if(Character.isUpperCase(word.charAt(0))) return true;        // upper
                    else return false;
                }
                else return true;       // lower
            }
        }
        else return true;
    }
}

class Main
{
    public static void main(String[] args)
    {
        Solution s = new Solution();
        String word = "A";
        System.out.println("result: " + s.detectCapitalUse(word));
    }
}


// logic
// for(int i=1; i<word.length(); i++)
// {
//     if(xor of chars[1:] == 1) return false;     // mix chars
//     else
//     {
//         if(and of chars[1:] == 1)
//         {
//             if(Character.isUpperCase(word.charAt(0))) return true;       // capital chars
//             else return false;
//         }
//         else return true;       // lower chars
//     }
// }
// // return true;
