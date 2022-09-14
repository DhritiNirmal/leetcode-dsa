#Shell Sort:
#The Shell sort algorithm allows you to sort elements that are apart from each other. The original sequence to sort the elements follows n/ 2, n/4, …, 1 sequence where n is the number of elements present in the unsorted list. For example, if you have a list of 8 elements, the length of that list will be divided by 2 i.e 8/ 2 = 4. Now, the first element will be compared with the element present at index number 4 and then, the gap will be produced by dividing 8 by 4. This time, the gap will be 2 and the elements that lie at these intervals will be compared. Finally, 8/ 8 = 1, so adjacent elements will be compared and sorted. (For odd number lists, the whole part of the quotient will be taken as the gap)

 

#Shell Sort Algorithm:

#Step 1: Find the value of the gap by dividing the number of elements by 2

#Step 2: Divide the given array into smaller sub-arrays having equal gap intervals

#Step 3: Using insertion sort, sort the sub-arrays

#Step 4: Repeat steps 1, 2 and 3 until the complete array is sorted

 

#Shell Sort Program:
def shsort(myarray, n):
    g = n // 2       # dividing the number of elements by 2 to find the gap
    while g > 0:
        for x in range(g, n):
            y = myarray[x]
            z = x
            while z >= g and myarray[z - g] > y:
                myarray[z] = myarray[z - g]
                z -= g
            myarray[z] = y
        g //= 2
mylist = [23, 12, 1, 17, 45, 2, 13]
length = len(mylist)
shsort(mylist, length)
print(mylist)
