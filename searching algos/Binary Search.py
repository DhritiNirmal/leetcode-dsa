#Binary Search:
#Binary Search is used to search for some given element in a sorted array by making use of the Decrease and Conquer Algorithm. Here, the key is looked for by first comparing it with the middle element and then dividing the array into half. The left half is searched if the element to be searched for is smaller than the middle element and vice versa. The appropriate sub-arrays are again divided into half and the process is repeated again.

#For example, if you have a sorted list of 8 elements, the key element will be compared with the element present at the middle or 7/ 2 = 3.5 (7 is the index value of the last element) and the whole number value is taken for comparison. So, the key element will be compared with the value present at index number 3 and if the given value is smaller, the same process is repeated towards the left side of the middle element and vice versa.

 

#Binary Search Algorithm:

#Step 1: Compare the key with the middle element

#Step 2: If matched, return the middle index value

#Step 3: If the key element is greater than the middle element, search for the key element towards the right of the middle element, else search to the left of it

 

Binary Search Program:
  def bin_search(mylist,key):
    l = 0
    r = len(mylist)-1
    matched = False
    while( l<=r and not matched):
        middle = (l + r)//2
        if mylist[middle] == key :
            matched = True
        else:
            if key < mylist[middle]:
                r = middle - 1
            else:
                l = middle + 1
    return matched
print(bin_search([2, 3, 56, 13, 1], 56))
print(bin_search([2, 3, 56, 13, 1], 26))
