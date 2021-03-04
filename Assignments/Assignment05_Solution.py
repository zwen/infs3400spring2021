

def checkPalindrome(text):
    reversed = ""
    for i in range(len(text)):
        reversed += text[len(text) - i - 1]

    print("you entered: ", text)
    print("in reverse it is: ", reversed)

    if text == reversed:
        return True
    else:
        return False

print("The result of the palindrome evaluation is (In True/False) :")
print(getPalindromeResult("mom"))
