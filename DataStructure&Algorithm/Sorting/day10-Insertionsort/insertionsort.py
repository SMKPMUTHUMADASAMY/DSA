#Insertion Sort
#Time complexity  =>O(n^2)
#space Complexity =>O(1)
Array=[7,1,5,4,3,2]
for i in range(1,len(Array)):
    curr=Array[i]
    j=i-1
    while j>=0 and curr<=Array[j]:
        Array[j+1]=Array[j]
        j-=1
    Array[j+1]=curr
print(Array)
