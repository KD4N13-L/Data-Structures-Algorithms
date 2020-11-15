def selection_sort(array):
    initial_length = len(array)
    for current_length in range(initial_length, 0, -1):
        max_index = 0
        for item in range(current_length):
            if array[item] > array[max_index]:
                max_index = item

        temp = array[max_index]
        array[max_index] = array[current_length - 1]
        array[current_length - 1] = temp

    return array


def main():

    array = input("Enter the number of array members, seperated by a coma")
    array = array.split(',')
    length = len(array)
    for item in range(length):
        array[item] = int(array[item])

    selection_sort(array)
    print(array)

main()