def add_digits(num):
    while num>=10:
        num =sum(int(digit) for digit in str(num))
    return num
num =int(input())
print(add_digits(num))