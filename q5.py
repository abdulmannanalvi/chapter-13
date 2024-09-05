from functools import reduce

l = [33,56,24,8,999,2224,478,22,578]

def Greater(a,b):
    if (a>b):
        return a
    return b

print (reduce(Greater,l))
