def merge(l, r):

    l_lenght = len(l)
    r_lenght = len(r)
    n = []

    i = 0
    j = 0

    while (i < l_lenght) and (j < r_lenght):
        if l[i] < r[j]:
            n.append(l[i])
            i += 1
        else:
            n.append(r[j])
            j += 1

    # Remainder of left list
    while i < l_lenght:
        n.append(l[i])
        i += 1

    # Remainder of right list
    while j < r_lenght:
        n.append(r[j])
        j += 1

    return n


def merge_sort(array):

    array_length = len(array)

    if array_length > 1:

        left_array = []
        right_array = []
        m = int(array_length / 2)

        for i in range(0, m):
            left_array.append(array[i])

        for j in range(m, array_length):
            right_array.append(array[j])

        left_array = merge_sort(left_array)
        right_array = merge_sort(right_array)

        return merge(left_array, right_array)

    else:
        return array


input_array = [1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]
print(input_array)

sorted_array = merge_sort(input_array)
print(sorted_array)
