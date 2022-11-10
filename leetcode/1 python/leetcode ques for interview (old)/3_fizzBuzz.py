class Solution:
    # def fizzBuzz(self, n: int) -> List[str]:
    def fizzBuzz(self, n: int):
        '''
            # i=0;
            # while(i<n):
            #     print(i)
            #     i+=1

            # str={"3": "Fuzz", "5": "Buzz", "15": "FizzBuzz"}
        '''

        list1=[]
        x,y,z=0,0,0
        for i in range(1,n+1):
            if i%15 == 0:
                list1.append('FizzBuzz')
            elif i%3 == 0:
                list1.append('Fizz')
            elif i%5 == 0:
                list1.append('Buzz')
            else: list1.append("%s" %i)

        print(list1)
        
        '''
            x+=1
            y+=1
            z+=1
            if z==15:
                print("FizzBuzz")
                z=0
            else:
                if x==3:
                    print("Fizz")
                    x=0
                if y==5:
                    print("Buzz")
                    y=0

                else: print(i+1)
        '''

        '''
            if z!=15:
                z+=1
                if x!=3: x+=1
                else:
                    print("Fizz")
                    x=0
                    y-=1
                    z-=1
                if y!=5: y+=1
                else:
                    print("Buzz")
                    y=0
                    x-=1
                    z-=1
            else: 
                print("FizzBuzz")
                z=0
                y-=1
                x-=1

            print(i+1)
        '''        
        
        
obj1=Solution()
obj1.fizzBuzz(15)