def checkio(text):
    
    # Modify the string, count occurences and define max and sorted clauses.
    letters = [k.lower() for k in text if k.isalpha()]
    d = {k: letters.count(k) for k in letters}
    highest = max(d.values())
    first = [k for k, v in d.items() if v == highest]
    if len(first) > 1:
        return min(sorted(first))
    else:
        return max(set(letters), key=letters.count)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

