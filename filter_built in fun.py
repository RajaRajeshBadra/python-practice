#Python has a built-in function ‘filter(f, a)’ that returns items of the list ‘a’ for whichf(item) returns true.
#an implementation for filter using list comprehensions


def startsWithR(element):
    if len(element) > 0:
             return element[0] == 'R'
    return False
    
names = ('Ram', 'Jill', 'ramesh', '')
ls=filter(startsWithR, names)
print(list(ls))
