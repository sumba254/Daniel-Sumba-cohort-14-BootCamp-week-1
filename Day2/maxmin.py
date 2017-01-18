def find_max_min(A):
    if min(A)== max(A):
        return [len(A)]
    else:
        return [min(A),max(A)]
find_max_min([2,3,5,7,1,10])