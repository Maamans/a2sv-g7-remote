def is_palindrome(x: int) -> bool:
    # Negative numbers are never palindrome
    if x < 0:
        return False

    original = x
    reversed_num = 0

    while x > 0:
        digit = x % 10          # get last digit
        reversed_num = reversed_num * 10 + digit
        x //= 10                 # remove last digit

    return original == reversed_num
