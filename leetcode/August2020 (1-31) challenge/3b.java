import java.util.*;

class Solution {
    public boolean isPalindrome(String s) {
        List<String> list = new ArrayList<String>();
        for(int i=0; i<s.length(); i++)
        {
            // int y = (int)s.charAt(i);
            // if((y>64 && y<91) || (y>96 && y<123) || (y>47 && y<58))
            //     list.add(String.valueOf(s.charAt(i)));
            if(Character.isLetterOrDigit(s.charAt(i)))
               list.add(String.valueOf(s.charAt(i)));
        }
        // System.out.println(list);

        int len = list.size();
        // System.out.println(len);
        int x=0;
        if(len%2 != 0)
        {
            for(int i=0; i<(len-1)/2; i++)
            {
                // System.out.println(i +"  "+ list.get(i));
                // System.out.println(len-1-i +"  "+ list.get(len-1-i) + "\n");
    
                if((list.get(i)).equalsIgnoreCase(list.get(len-1-i))) x++;
            }
            System.out.println("x: " + x);
            if(x==(len-1)/2) return true;
        }
        else
        {
            for(int i=0; i<len/2; i++)
            {
                // System.out.println(i +"  "+ list.get(i));
                // System.out.println(len-1-i +"  "+ list.get(len-1-i) + "\n");
    
                if((list.get(i)).equalsIgnoreCase(list.get(len-1-i))) x++;
            }
            System.out.println("x: " + x);
            if(x==len/2) return true;
        }
        return false;
    }
}

class Main
{
    public static void main(String[] args)
    {
        Solution so = new Solution();
        String s = "A man, a plan, a canal: Panama";
        System.out.println(so.isPalindrome(s));
    }
}
