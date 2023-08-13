#### Bubble Sort ####

'''

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, 
compares adjacent elements, and swaps them if they are in the wrong order. 
The pass through the list is repeated until no swaps are needed, 
indicating that the list is now sorted. 

Here's an implementation of Bubble Sort in Python:

'''

list = [5,1,4,2,7]

for i_loop in range(len(list)):
    for i_swap in range(i_loop, len(list)-1): 
        if list[i_swap] > list[i_swap + 1]: #compare the adjacent element
            list[i_swap], list[i_swap+1] = list[i_swap+1], list[i_swap]
        
            
print(list)

''' This is the standard process of Bubble Sort used to sort elements in ascending order. 
    (which is the more common use case for Bubble Sort)'''