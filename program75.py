def palindrome(s, start, end):
    if start >= end:
        return True

    if s[start] != s[end]:
        return False

    return palindrome(s, start + 1, end - 1)


text = input("Enter a string: ")

if palindrome(text, 0, len(text) - 1):
    print("It is a palindrome")
else:
    print("It is not a palindrome")