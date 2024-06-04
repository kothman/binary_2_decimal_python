def binary_to_decimal(binary_number_text) -> str:
    decimal_number: int = 0
    # starting from small to big, working backwards in the string
    # each one and zero is summed up based on position
    # 2*n^0 + 2*n^1 + 2*n^2 ...
    for i in range(len(binary_number_text)):
        decimal_number += int(binary_number_text[ -1 - i ])*(2**i)
    return str(decimal_number)

def binary_int_to_decimal_int(binary_number: int) -> int:
    decimal_number: int = 0
    i: int = 0
    while binary_number > 0:
        if binary_number % 2 == 1:
            decimal_number += 2 ** i
        i += 1
        binary_number //= 10
    return decimal_number

def is_binary(num_str: str) -> bool:
    # make sure each character is a 1 or 0
    for c in num_str:
        if (c != '1' and c != '0'):
            return False
    return True

def main():
    # Get input from user, and keep looping until they enter a valid binary number
    binary_number_text: str = input('Please enter a binary number: ')
    while binary_number_text.isdigit() == False or is_binary(binary_number_text) == False:
        print('Please enter a valid binary number')
        binary_number_text = input()
    # Get the decimal number
    decimal_number_text = binary_to_decimal(binary_number_text)
    decimal_number = binary_int_to_decimal_int(int(binary_number_text))
    # Print the binary and decimal number
    print(f'{binary_number_text} in decimal is {decimal_number_text}')
    print(f'{binary_number_text} in decimal is {decimal_number}')

if __name__ == '__main__':
    main()
