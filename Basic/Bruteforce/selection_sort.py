
#Selecting the max and moving it to the end of the array
array = [3,4,1,2,7,9]
for i in range(len(array)):
    # print('i', i)
    min = i
    for j in range(i+1, len(array)):
        # print('j', j)
        if array[min] > array[j]:
            min = j
    array[i],array[min] = array[min], array[i]
print(array)

#Selecting the max and moving it to the end of the array
array = [3,4,1,2,7,9]
n = len(array)
for i in reversed(range(len(array))):
    # print('i', i)
    max = i
    for j in range(0, i-1):    
        if array[max] < array[j]:
            max = j
            # print('max', max)
    array[i],array[max] = array[max], array[i]
print(array)