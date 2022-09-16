#Searching Algorithms:
#Searching algorithms are used to search for or fetch some elements present in some given dataset. There are many types of search algorithms such as Linear Search, Binary Search, Exponential Search, Interpolation search, etc.

#Linear Search:
#The Linear Search algorithm is used to successively search for a given element by comparing it with each element of the given array. It is one of the simplest searching algorithms but very important so as to understand other sorting algorithms.

 

#Linear Search Algorithm:

#Step 1: Create a function that will accept the data list, the length of the list and the key element

#Step 2: If an element present in the given list matches the key element, return the corresponding index number

#Step 3: If the element is not found, return -1

Linear Search Program:

def lin_search(myarray, n, key): 
   
    for x in range(0, n): 
        if (myarray[x] == key): 
            return x 
    return -1
   
myarray = [ 12, 1, 34, 17]
key = 17
n = len(myarray)
matched = lin_search(myarray, n, key) 
if(matched == -1): 
    print("Key is not present") 
else: 
    print("Key is present in the given list at index", matched)
OUTPUT: Key is present in the given list at index 3
