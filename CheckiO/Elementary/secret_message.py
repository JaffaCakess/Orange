import re
def find_message(text):

    capital_letters = re.findall("[A-Z]", text)
    return "".join(capital_letters)

if __name__ == '__main__':
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
