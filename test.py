#   Copyright (c) 2020. Ioannis E. Kommas. All Rights Reserved
def DecimalToBinary(num):
    if num > 1:
        DecimalToBinary(num // 2)
    print(num % 2, end='')


# Driver Code
if __name__ == '__main__':
    # decimal value
    dec_val = 24

    # Calling function
    DecimalToBinary(dec_val)
