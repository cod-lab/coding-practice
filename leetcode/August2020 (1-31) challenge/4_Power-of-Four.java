import java.lang.Math; 

class Solution {
    public boolean isPowerOfFour(int num) {
        // System.out.println("\nnum: " + num);
        if(num>0)
        {
            if(num == 1) return true;

            String x = Integer.toBinaryString(num);
            int a = Integer.parseInt(x);
            System.out.println("a: " + a);
            System.out.println("a<<1: " + (a<<1));
            // int c = Integer.parseInt(x);
            // System.out.println("c: " + c);
            // int d = ~c;
            // System.out.println("d: " + d);
            // int len = x.length();
            // String y = x.substring(1,len);
            // // int b = y.length();
            // long c = Long.parseLong(x);
            // System.out.println("c: " + (String.valueOf(c)));
            // // System.out.println("\ny: " + y);
            // // System.out.println("\nb: " + b);
            // String a = "0".repeat(len-1);
            // if(a.equals(y))
            // {
            //     if((len-1)%2 == 0)
            //     {
            //         // System.out.println("sub-string: " + x.substring(1, x.length()));
            //         return true;
            //     }
            // }
        }
        return false;
    }
}

class Main
{
    public static void main(String[] args)
    {
        Solution s = new Solution();
        int num = -1;
        while(num<5)
        {
            int i =(int) Math.pow(4, num);
            System.out.println(num + " :\t" + i + " :\t" + s.isPowerOfFour(i));
            // System.out.println(num + " :\t" + s.isPowerOfFour(num));
            ++num;
        }
        // System.out.println(num + ":\t" + s.isPowerOfFour(num));
    }
}

// DECIMAL
// 4^0 = 1         1/4=1/4
// 4^1 = 4         4/4=1
// 4^2 = 16        16/4=4
// 4^3 = 64        64/4=16
// 4^4 = 256
// 4^5 = 1024

// BINARY
// 0 :	1 :	1
// 1 :	4 :	100
// 2 :	16 :	10000
// 3 :	64 :	1000000
// 4 :	256 :	100000000
// 5 :	1024 :	10000000000
// 6 :	4096 :	1000000000000
// 7 :	16384 :	100000000000000
// 8 :	65536 :	10000000000000000
// 9 :	262144 :	1000000000000000000
// 10 :	1048576 :	100000000000000000000
// 11 :	4194304 :	10000000000000000000000
// 12 :	16777216 :	1000000000000000000000000
// 13 :	67108864 :	100000000000000000000000000
// 14 :	268435456 :	10000000000000000000000000000
// 15 :	1073741824 :	1000000000000000000000000000000
// 16 :	2147483647 :	1111111111111111111111111111111
// 17 :	2147483647 :	1111111111111111111111111111111
// 18 :	2147483647 :	1111111111111111111111111111111
// 19 :	2147483647 :	1111111111111111111111111111111

// 000000000000000000000000000000
