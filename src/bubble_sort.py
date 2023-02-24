def bubble_sort(array):

    change_place = True
    while change_place != False:

        change_place = False
        for i in range(0, len(array) - 1, 1):

            if array[i] > array[i + 1]:
                tmp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = tmp
                change_place = True
                print(array)


a = [1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]

bubble_sort(a)