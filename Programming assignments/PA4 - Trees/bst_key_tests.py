from bst import *


if __name__ == "__main__":
    k1 = MyComparableKey(1, "one")
    k2a = MyComparableKey(2, "two")
    k2b = MyComparableKey(2, "two")
    print(k1 < k2a)
    print(k2b < k1)
    print(k2a < k2b)
    print(k2b < k2a)
