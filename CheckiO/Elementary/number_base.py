
def checkio(str_number, radix):

    try: return int(str_number, radix)
    except ValueError: return -1

if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex" # 10*16**1=160, 15*16**0=15, =175
    assert checkio("101", 2) == 5, "Bin" # 0101(2**0=1, 2**2=4, =5)
    assert checkio("101", 5) == 26, "5 base" # 0101(5**0=1, 5**2=25, =26)
    assert checkio("Z", 36) == 35, "Z base" # 35*36**0=35
    assert checkio("AB", 10) == -1, "B > A > 10"
                   # start from right to left; "AF" A = 1(10*16**1), F = 0(15*16**0), "AB" A = 1, B = 0