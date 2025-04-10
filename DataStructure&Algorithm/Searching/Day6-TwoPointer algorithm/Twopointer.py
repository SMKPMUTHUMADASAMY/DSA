""" Two Pointer Algorthim """
#Time Complexity =o(n)
#Space Complexity=o(n)
array=[1,2,3,4,5,6,7]
Target=6
L=0
R=len(array)-1
Flag=1
while (L<R):
    sum=array[L]+array[R]
    if sum==Target:
       Flag=0
       print(L,R)
       break
    elif sum<Target:
        L=L+1
    elif sum>Target:
        R=R-1
if Flag==1:
    print("Target Not Found")
