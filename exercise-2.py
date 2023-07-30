def index_power(numnbers, n):
    # check the length of the list.
    # there are 2 conditions: 1. when the length list > n 2. when the length list < 2
    # for condition 1: return list[n] ** n
    # for condition 2: return -1
    if len(numnbers) > n:
        return numnbers[n] ** n
    else:
        return -1
print(index_power([1, 2], 3))