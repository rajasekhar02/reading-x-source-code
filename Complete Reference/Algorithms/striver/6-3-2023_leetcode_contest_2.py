#


def solution(a):
    b = []

    for i in range(0, (len(a) >> 1)):
        b.append(a[i])
        b.append(a[len(a) - i - 1])
    if len(a) & 1:
        b.append(a[(len(a) >> 1)])

    # conditions to check whether the list is sorted or not
    # list contains values in range 10^-9 to 10^9
    for i in range(1, len(b)):
        # if both numbers are negative then if the i-1 th element
        # greater than or equal i th element then list is not in sorted order
        if b[i - 1] < 0 and b[i] < 0 and b[i - 1] >= b[i]:
            return False
        # otherwise i-1 th element greater than or equals to the i th element
        # then list is not in sorted order
        if b[i - 1] >= b[i]:
            return False
    return True
