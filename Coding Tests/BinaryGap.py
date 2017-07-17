'''
Test to find the largest binary gap.
'''


def binary_gap(n):
    binary_val = bin(n)
    binary_one = binary_val[2:]
    bin_gap = 0
    temp_gap = 0
    length = len(binary_one)
    print("This is your binary value:\n" + binary_one)

    for i in range(length):
        if binary_one[i] == '0':  # if in gap, increase gap count
            bin_gap += 1

        if binary_one[i] == '1':  # beginning/end of gap count
            if temp_gap <= bin_gap:
                temp_gap = bin_gap
            bin_gap = 0  # set back to zero after finding a 1 value

    return temp_gap


print(binary_gap(1376796946))