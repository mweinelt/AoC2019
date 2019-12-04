#!/usr/bin/env python3

def digits_from_number(number):
    digits = []
    while number:
        digits.append(number % 10)
        number //= 10
    return list(reversed(digits))

def has_adjacent_double(digits):
    has_double = False
    for i in range(len(digits) - 1):
        if digits[i] == digits[i+1]:
            try:
                left_differs = digits[i-1] != digits[i]
            except IndexError:
                left_differs = True

            try:
                right_differs = digits[i+2] != digits[i]
            except IndexError:
                right_differs = True

            if left_differs and right_differs:
                return True
    return False

def has_no_ltr_decrease(digits):
    for i in range(len(digits) - 1):
        if digits[i] > digits[i+1]:
            return False
    return True

def num_passwords_in_range(start, end):
    n = 0
    for candidate in range(start, end + 1):
        digits = digits_from_number(candidate)

        if has_adjacent_double(digits) and has_no_ltr_decrease(digits):
            n += 1
    return n


if __name__ == '__main__':
    for x in (111111, 223450, 123789, 112233, 123444, 111122):
        digits = digits_from_number(x)
        print(f"{x} adjacent doubles? {has_adjacent_double(digits)}")
        print(f"{x} no ltr decrease? {has_no_ltr_decrease(digits)}")

    print(num_passwords_in_range(240298, 784956))
