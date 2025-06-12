
#Bubbling moving it to the end of the array
array = [3,4,1,2,7,9]
for i in range(len(array)):
    print('i', i)
    for j in reversed(range(i+1, len(array))):
        print('j', j)
        if array[j] < array[j-1]:
            array[j-1],array[j] = array[j], array[j-1]
        print(array)
print(array)