
#Bubbling moving it to the end of the array
array = [8,2,4,9,3,6]
for i in range(len(array)):
    temp = array[i]
    j=i-1
    print('i', i)
    print('temp', temp)
    while array[j] > temp and j >=0:
        array[j+1] = array[j]
        j = j-1
        print(array)
    array[j+1] = temp
print(array)