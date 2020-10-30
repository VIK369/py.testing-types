#python programe that
#to find largest number in a list
def mymax(list1):
    '''
    >>> mymax([3,4,7,100])
    100

    '''
    #we innitialize fist number as the largest adn the compare
    #every othe rnum to it
    max = list1[0]
    #this is were we conpare each num to the initialized max
    for x in list1:
        if x > max :
            max = x
            #after complete transversing the list
            #return the 'Max' value(new)
    return max

#driver code
list1 = [10,20,4,45,99]
print("Largest element is:" , mymax(list1))
