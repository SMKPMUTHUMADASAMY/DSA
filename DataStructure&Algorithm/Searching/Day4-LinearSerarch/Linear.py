#Linear Search Algorithm
array=[1,2,3,4,5]
x=3
for i in range(0,len(array)):
    if array[i]==x:
        print("Searching Element Present in " ,array[i],"array position")
        break
else:
    print("Target Value Not Found")
