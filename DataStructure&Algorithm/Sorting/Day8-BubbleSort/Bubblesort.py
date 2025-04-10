#Bubble Sort
#Time Complexity =>o(n)
#Space Complexity =>o(1)
print("Bubble sort Using for LooP")
Array=[11,9,6,1,2,7]
for i in range(0,len(Array)-1):
     for j in range(0,len(Array)-1):
         if Array[j]>Array[j+1]:
             Array[j],Array[j+1]=Array[j+1],Array[j]
print(Array)
print("\nBubble sort Using While LooP")
 
while(True):
     flag=1
     for i in range(0,len(Array)-1):
         if (Array[i]>Array[i+1]):
               Array[i],Array[i+1]=Array[i+1],Array[i]
               flag=0
     if flag==1:
         break
print(Array)
             
      
    
