from functools import reduce
def checkio(number):

    return reduce(lambda x,y:x*y,[int(x)for x in str(number).replace("0","")])

if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1