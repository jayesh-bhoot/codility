## List Number -> List
## Given a list and an integer n, produce a list by rotating the given list n times


def rotate(l, k):
    if not l or k == 0:
        return l
    r = k % len(l)
    return l[-r:] + l[0:-r]


if __name__ == '__main__':
    # n=k
    ## n=k=0
    assert rotate([], 0) == []
    ## n=k>0
    assert rotate([1, 2, 3, 4], 4) == [1, 2, 3, 4]

    # n<k
    ## n=0, k>0
    assert rotate([], 5) == []
    ## n>0, k>0
    assert rotate([-5, -4, -3, -2, -1, 0], 8) == [-1, 0, -5, -4, -3, -2]
    ## failed test iterations for k>=n => n<=k: got [1, 1, 2, 3, 5] expected [3, 5, 1, 1, 2]
    ## try a k>n*2
    assert rotate([3, 5, 1, 1, 2], 14) == [5, 1, 1, 2, 3]


    # n>k
    ## n>0, k=0
    assert rotate([1, 2, 3], 0) == [1, 2, 3]
    # n>0, k>0
    assert rotate([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]

    # same elements in n
    assert rotate([0, 0, 0], 4) == [0, 0, 0]

    
