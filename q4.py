def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1,45,68,115,335,23,56,55]
f = list(filter(divisible5,a))
print(f)