
def checkio(data):

    roman_numerals = (('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
                      ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
                      ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1))
    result = ""
    for numeral, integer in roman_numerals:
        while data >= integer:
            result += numeral
            data -= integer
    return result

if __name__ == '__main__':
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'