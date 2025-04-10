#Selection Sort
#Time complexity=>O(n^2)
#Space Complexity=>O(1)
Array=[4,5,2,3,1,4,0,6]
for pos in range(0,len(Array)-1):
    min=pos
    for i in range(pos,len(Array)):
        if Array[i]<Array[min]:
            min=i
    Array[min],Array[pos]=Array[pos],Array[min]
print(Array)
