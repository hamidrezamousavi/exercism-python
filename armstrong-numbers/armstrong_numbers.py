def is_armstrong_number(number):
    number_as_string = str(number)
    numberOfDigit = len(number_as_string)
    sum = 0
    for digit in number_as_string:
        sum += int(digit) ** numberOfDigit
    if sum == number:
        return True
    return False


