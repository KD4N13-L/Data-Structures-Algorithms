def mergesort(array):
    if len(array) == 1:
        return array
    else:
        if len(array) % 2 == 0:
            array1 = []
            half = (int(len(array) / 2))
            for index in range(0, half):
                array1.append(array[index])
            array2 = []
            for index in range(half, len(array)):
                array2.append(array[index])
            array1 = mergesort(array1)
            array2 = mergesort(array2)
            return merge(array1, array2)
        else:
            array1 = []
            half = (int((len(array) + 1) / 2))
            for index in range(0, half):
                array1.append(array[index])
            array2 = []
            for index in range(half, len(array)):
                array2.append(array[index])
            array1 = mergesort(array1)
            array2 = mergesort(array2)
            return merge(array1, array2)


def merge(array1, array2):
    temp_array = []
    while array1 and array2:
        if array1[0] > array2[0]:
            temp_array.append(array2[0])
            array2.pop(0)
        else:
            temp_array.append(array1[0])
            array1.pop(0)
    while array1:
        temp_array.append(array1[0])
        array1.pop(0)
    while array2:
        temp_array.append(array2[0])
        array2.pop(0)

    return temp_array


def main():
    array = input("Enter the number of array members, seperated by a coma")
    array = array.split(',')
    length = len(array)
    for item in range(length):
        array[item] = int(array[item])

    print(mergesort(array))


main()
