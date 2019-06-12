## List -> Number
## Given a list of an odd-numbered length filled with integers,
## which has all but one paired integers, produce the unpaired integer. 

"""
O(n log n) + O(n) + O(n)*O(n)
=> O(n log n) + O(n) + O(n^2)
=> O(n^2)
"""

def odd_one_out_old(l):
    sorted_l = sorted(l)
    unique_vals = set(sorted_l)
    return next((x for x in unique_vals if sorted_l.count(x) % 2 == 1), None)

def odd_one_out(l):
    m = {}

    for x in l:
        if x in m:
            m[x] += 1
        else:
            m[x] = 1

    for k, v in m.items():
        if v % 2 == 1:
            return k
    return None


if __name__ == '__main__':
    assert odd_one_out([9]) == 9
    assert odd_one_out([55, 55, 2]) == 2
    assert odd_one_out([3, 66, 66]) == 3
    assert odd_one_out([77, 889, 77]) == 889
    assert odd_one_out([5, 2, 0, 93, 0, 2, 5]) == 93
    assert odd_one_out([5, 5, 0, 5, 0, 5, 5]) == 5
