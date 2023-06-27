def recurse(disks, src, via , dest):
    if disks > 0:
        # step 1: move n-1 disks from 1 to 2 using 3
        lis = recurse(disks-1, src, dest, via)
        # step 2: move nth disk from 1 to 3
        lis.append([src, dest])
        # step 3: again move n-1 disks from 2 to 3 using 1
        lis2 = recurse(disks-1, via, src, dest)
        lis = [*lis, *lis2]
        return lis
    return []
def towerOfHanoi(n):
    #  i will move n disks from 1 to 3 using 2
    return recurse(n, 1, 2, 3)
print(towerOfHanoi(3))