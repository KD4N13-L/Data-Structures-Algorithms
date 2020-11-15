def dict_list_bubble_sort(array):
    def bubble_sort(array, sort_option):
        initial_length = len(array)
        swaps = 1
        for current_length in range(initial_length, 1, -1):
            if swaps != 0:
                swaps = 0
                for index1 in range(current_length - 1):
                    index2 = index1 + 1
                    if array[index1][''+sort_option+''] > array[index2][''+sort_option+'']:
                        temp = array[index1]
                        array[index1] = array[index2]
                        array[index2] = temp
                        swaps += 1
            else:
                break
        return array

    print("According to what would you like to sort the dictionaries?")
    print("1: Page Count")
    print("2: Publishing Year")
    setting = int(input("Choose one of the options above --- "))
    print()
    if setting == 1:
        option = "pages"
        bubble_sort(array, option)
    elif setting == 2:
        option = "publish_year"
        bubble_sort(array, option)
    else:
        print("Try again. Your choice was incorrect")


def dict_list_print(array):
    for dictionary in array:
        print(dictionary["name"])
        print("Page Count: ", dictionary["pages"], "- Published in: ", dictionary["publish_year"])
        print()


def main():

    return_of_the_king = {"name": "Lord of the Rings: Return of the King", "pages": 416, "publish_year": 1955}
    deathly_hallows = {"name": "Harry Potter and the Deathly Hallows", "pages": 607, "publish_year": 2007}
    jon_livingston_seagull = {"name": "Jonathan Livingston Seagull", "pages": 144, "publish_year": 1970}
    array = [return_of_the_king, deathly_hallows, jon_livingston_seagull]

    dict_list_bubble_sort(array)
    dict_list_print(array)


main()
