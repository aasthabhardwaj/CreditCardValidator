from datetime import datetime

# Name can contain only alphabets and spaces
def isNameValid(name):
    for character in name:
        if not (character.isalpha() or character == ' '):
            print("Error: Name can only contain alphabets and spaces!")
            return False  
    return True

#Card should be Valid according to luhn algo
def isCardValid(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    if checksum % 10 == 0:
        return True
    print("Error: Invalid Card Number!")
    return False

# CVV shoul be between 100 and 10000
def isCvvValid(cvv):
    if 100 < cvv < 10000:
        return True
    print("Error : Invalid CVV!")
    return False

# Date should be equal or more than the current date 
def isExpDateValid(exp_date):
    try:
        exp_month = int(exp_date.split('/')[0])
        exp_year = int(exp_date.split('/')[1])
    except:
        print("Error: Date format invalid!")
        return False

    curr_month = datetime.now().month
    curr_year = datetime.now().year % 100

    if curr_year < exp_year or (curr_year == exp_year and curr_month < exp_month):
        return True
    print("Error: Your Card has expired!")
    return False

#Function that gets called
def isValid(user_info):
    return isNameValid(user_info['user_name']) and isCardValid(
        user_info['card_number']) and isCvvValid(int(user_info['cvv'])) and isExpDateValid(
        user_info['valid_until'])


#Taking input from the user
if __name__ == '__main__':
    user_info = {'user_name': input("Enter name of the Card Holder: "),
                 'card_number': input("Card number: "),
                 'cvv': input("CVV of the Card: "),
                 'valid_until': input("Valid until (MM/YY): ")}
    print("Successfully validated card details") if isValid(user_info) else print("Information Falied! Please Try again!")
