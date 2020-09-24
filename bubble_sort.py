def dict_list_bubble_sort(array):
    initial_length = len(array)
    swaps = 1
    for current_length in range(initial_length, 1, -1):
        if swaps != 0:
            swaps = 0
            for index1 in range(current_length - 1):
                index2 = index1 + 1
                if array[index1]["publish_year"] > array[index2]["publish_year"]:
                    temp = array[index1]
                    array[index1] = array[index2]
                    array[index2] = temp
                    swaps += 1
        else:
            break
    return array


def dict_list_print(array):
    for dictionary in array:
        print(dictionary["name"], "- Published in", dictionary["publish_year"])


def main():
    return_of_the_king = {"name": "Lord of the Rings: Return of the King", "publish_year": 1955}
    deathly_hallows = {"name": "Harry Potter and the Deathly Hallows", "publish_year": 2007}
    jon_livingston_seagull = {"name": "Jonathan Livingston Seagull", "publish_year": 1970}

    array = [return_of_the_king, deathly_hallows, jon_livingston_seagull]

    dict_list_bubble_sort(array)
    dict_list_print(array)


main()
