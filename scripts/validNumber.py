def isValidNumber(number):
    try:
        numberList = list(str(number))
        if len(set(numberList)) == 4:
            return True
        return False
    except:
        return False