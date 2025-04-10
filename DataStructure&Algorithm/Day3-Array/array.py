#array Module
from array import*
#array Declaration
arr=array('i',[1,2,3,4,5,6,7,8,9])
print(arr)
#Aceesing Array Elerment
print(arr[5])
#inserting Element in an array
arr.insert(8,5)
print(arr)
#Delete The Array eLement
print(arr.pop(2))
#Search Array Element
value=3
for i in range(0,len(arr)):
    if arr[i]==value:
        print(arr[i])
        break
else:
    print("Value Not found in Array")
