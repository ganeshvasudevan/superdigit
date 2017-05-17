#!/usr/bin/python

def calc_digit_sum(number):
    digits = []
    while number:
        digits.append(number - (number / 10) * 10)
        number = number / 10

    sum = 0
    for digit in digits:
        sum += digit
    return sum

def calculate_super_digit(number):
    if number < 10:
        return number
    return calculate_super_digit(calc_digit_sum(number))


def main():
    k = input("enter the value of k  ")
    n = input("enter the value of n  ")

    k_super_digit = calculate_super_digit(k)
    result = calculate_super_digit(k_super_digit * n)
    print 'super digit of (k, n): ({}, {}) is {} \n'.format(k, n, result)

if __name__ == '__main__':
	main()

