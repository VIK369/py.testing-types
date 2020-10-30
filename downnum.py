def descending(x):


    '''
    >>> descending([1,2,3,4,5,6,7,8,9,10,11,])
    [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    '''


    y = sorted(x)
    return y[::-1]
x = [3,5,99,91,2,78]
print(descending(x))