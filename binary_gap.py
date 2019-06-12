## Number -> Number
## Given an integer, return the length of the longest sequence of 0's between two 1's in its binary equivalent.
## Return 0 if no such sequence exists.


def longest_binary_gap(num):
    gaps = bin(num).strip('0').split('1')[1:]
    if gaps:
        return len(max(gaps))
    else:
        return 0


if __name__ == '__main__':
    assert longest_binary_gap(0) == 0
    assert longest_binary_gap(1) == 0
    assert longest_binary_gap(9) == 2
    assert longest_binary_gap(15) == 0
    assert longest_binary_gap(20) == 1
    assert longest_binary_gap(32) == 0
    assert longest_binary_gap(529) == 4
    assert longest_binary_gap(545) == 4
    assert longest_binary_gap(2181) == 4
    assert longest_binary_gap(1041) == 5



assert solution(0) == 0
assert solution(1) == 0
assert solution(9) == 2
assert solution(15) == 0
assert solution(20) == 1
assert solution(32) == 0
assert solution(529) == 4
assert solution(545) == 4
assert solution(2181) == 4
assert solution(1041) == 5
