// import java.util.*;

class Solution {
    public boolean isPalindrome(String s) {
        // List<String> list = new ArrayList<String>();
        int y=0,x=0,j=0,k=s.length()-1;
        for(int i=0; i<s.length()/2; i++)
        {
            // int y = (int)s.charAt(i);
            // if((y>64 && y<91) || (y>96 && y<123) || (y>47 && y<58))
            //     list.add(String.valueOf(s.charAt(i)));
            if(!Character.isLetterOrDigit(s.charAt(j)))
            {
                // j++;
                System.out.println("for j: " + s.charAt(j++));
            } 

            else if(!Character.isLetterOrDigit(s.charAt(k-i)))
            {
                k--;
                System.out.println("for k: " + s.charAt(k-i));
            }

            else
            {
                System.out.println("for else i: " + i + "- " + s.charAt(j));
                System.out.println("for else len-i: " + (k-i) + "- " + s.charAt(k-i));

                y++;
                if(s.charAt(j) == s.charAt(k)) x++;
            }
            j++;
            k--;
            System.out.println("\n");
        }
        System.out.println("x: " + x + " y: " + y + " j: " + j + " k: " + k);
        if(x==y) return true;
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
