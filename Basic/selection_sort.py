array = [3,4,1,2,7,9]
for i in range(len(array)):
    print('i', i)
    min = i
    for j in range(i+1, len(array)):
        print('j', j)
        if array[min] > array[j]:
            min = j
    array[i],array[min] = array[min], array[i]
    print(array)