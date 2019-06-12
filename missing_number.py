## List -> Integer
## Given a list of length n, find the missing value.


def missing_number(l):
    cons_sum = int(((1 + len(l)) / 2.0) * len(l))
    lst_sum = sum(l) - (len(l) + 1)
    return cons_sum - lst_sum


def missing_number_2(l):
    sl = sorted(l)
    for i, n in enumerate(sl, start=1):
       if i != n:
           return i


if __name__ == '__main__':
    assert missing_number([]) == 1
    assert missing_number([2]) == 1
    assert missing_number([2, 3]) == 1
    assert missing_number([3, 1]) == 2
    assert missing_number([2, 4, 1]) == 3
    assert missing_number([3, 2, 4]) == 1
