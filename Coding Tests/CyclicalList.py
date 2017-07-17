__author__ = 'adam0954'
'''
Cycles through a list/array, taking the last element
and inserting it into the first index, of a zero based array.
A being the array, and K the count of times to shift
'''

def cyclical_list(A, K):  # Stack approach to the problem
    count = K
    list_one = A
    list_two = []
    if count < len(list_one) and len(list_one) > 1:  # handles submissions of empty arrays and single elements
        for i in range(count):
            if i == 0:
                v = list_one.pop()
                list_two.append(v)
            else:
                list_two.insert(0, list_one.pop())

    else:
        return list_one

        list_two.extend(list_one)

    return list_two


def cyclical_list_short(A, K):  # shorter, and more abbreviated way of processing the element shift via slciing
    if len(A) == 0:
        return A

    K = K % len(A)

    return A[-K:] + A[: -K]


test_list = [ i for i in range(1,100)]
test_list2 = [3, 8, 9, 7, 6, 4, 5, 7,9]

print(cyclical_list(test_list, 9))
print(cyclical_list_short(test_list2,3))


