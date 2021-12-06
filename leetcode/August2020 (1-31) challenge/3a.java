class Solution {
    public boolean isPalindrome(String s) {
        int n = s.length();
        // System.out.println(n);

        String[] word; // = new Stringr[n];
        int j = 0;
        for(int z=0; z<n; z++)
        {
            int y = (int)s.charAt(z);
            if((y>64 && y<91) || (y>96 && y<123))
            {
                word[j] = String.valueOf(s.charAt(z));
                // word[j] = s.charAt(z);
                j++;
            }
        }
        // for(int i=0; i<word.length; i++)
        //     System.out.println(word[i]);
// Character.
        int p = word.length;
        System.out.println(p);
        int x=0;
        for(int i=0; i<(p-1)/2; i++)
        {
            System.out.println("s: " + word[i] +"\te: "+ word[p-1-i]);
            // System.out.println(word[p-1-1]);
            // System.out.println(i +"  "+ word[i]);

            if(word[i] == word[p-1-i]) x++;
        }

        // int x=0;
        // for(int i=0; i<((n-1)/2)+2; i++)
        // {
        //     int y = (int)s.charAt(i);
        //     if((y>64 && y<91) || (y>96 && y<123))
        //     {
        //         System.out.println(i +"  "+ s.charAt(i) +"  "+ y);
        //         if(s.charAt(i) == s.charAt(n-1-i))
        //         {
        //             x++;
        //         }
        //         // i++;
        //     }
        //     // else i++;
        // }
        System.out.println("x: " + x);

        if(x==(p-1)/2)
        {
            return true;
        }
        else return false;
    }
}

class Main
{
    public static void main(String[] args)
    {
        Solution so = new Solution();
        String s = "a man, a plan, a canal: panama";
        System.out.println(so.isPalindrome(s));
    }
}
