def xSort(val):
    return val[1]

tlist = [(2, 3), (1, 4), (5, 2)]

tlist.sort(key=xSort)

print(tlist)