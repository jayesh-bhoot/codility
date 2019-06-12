## List -> Integer

"""
Given
1) that a list L of N integers where:
    2 <= N <= 100000;
    -1000 <= L[i] <= 1000,
2) that L is split at a position P where:
    0 < P < N (cant be split at 0th and last elements),
3) and that the absolute difference of the sums of the split parts S1 and S2,
Calculate the minimal difference between the splits at different positions across the list.
"""


# O(N)
def minimum_viable_split(l):
    diffs = []
    sum1, sum2 = 0, sum(l)
    for x in l[:-1]:
        sum1 += x
        sum2 -= x
        diffs.append(abs(sum1 - sum2))
    return min(diffs)


# O(N^2)
def minimum_viable_split_ON2(l):
    diffs = []
    for x in range(1, len(l)):
        diffs.append(abs(sum(l[0:x]) - sum(l[x:])))
    return min(diffs)


if __name__ == "__main__":
    assert minimum_viable_split([3, 1, 2, 4, 3]) == 1
    assert minimum_viable_split([-1000, 10]) == 1010
    assert minimum_viable_split([10, 10, 10, 10, 10]) == 10
    assert minimum_viable_split([0, 0, 0, 0]) == 0
    assert minimum_viable_split([0, 0, 5, 0]) == 5
    assert minimum_viable_split([10, 10, 10, 10, 10, 10]) == 0
    assert minimum_viable_split([-100, 300, 40, -1000, 400]) == 160
    assert minimum_viable_split([-1000, 300, 40, -100, 400]) == 960
    assert minimum_viable_split([-1000, -100, 40, 300, 400]) == 1160

