## Integer Integer Integer -> Integer
## given initial position x, destined position y, where y>=x and 1>=x,y>=1,000,000,000,
## and leap-length l,
## calculate the minimium number of leaps n to reach from x to >=y.

from math import ceil

def frog_jump(x, y, l):
    if x == y:
        return 0
    return int(ceil((y - x) / float(l)))


if __name__ == "__main__":
    assert frog_jump(1, 10, 1) == 9
    assert frog_jump(1, 10, 9) == 1
    assert frog_jump(100, 100, 1000) == 0
    assert frog_jump(1, 10, 12) == 1
    assert frog_jump(1, 1000000000, 1) == 999999999
    assert frog_jump(1, 1000000000, 1000000) == 1000
