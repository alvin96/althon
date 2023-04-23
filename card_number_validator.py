
# Luhn’s algorithm
def cardNumberChecksum(card_number):
    checksum = 0
    card_number = card_number.replace(" ", "")
    digitArr = strToIntArray(card_number)
    odd_digit = digitArr[-1::-2]
    even_digit = digitArr[-2::-2]

    checksum += sum(odd_digit)
    for digit in even_digit:
        checksum += sum(strToIntArray(digit * 2))
    return checksum % 10


def strToIntArray(card_number):
    return [int(digit) for digit in str(card_number)]


if __name__ == "__main__":
    card_number = input("Please enter your credit / debit card number: ")
    # card_number = "1234 1234 1234 1234"
    isValidCard = cardNumberChecksum(card_number)

    if isValidCard == 0:
        print("Card number valid")
    else:
        print("Invalid card number")
