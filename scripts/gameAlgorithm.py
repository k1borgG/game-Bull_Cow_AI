from scripts.validNumber import isValidNumber
import random

def gameAI(numberForGuess, i_cow, i_bull):
    number_guest_list = list(str(numberForGuess))
    for index in range(len(number_guest_list)):
        if index not in i_bull and index in i_cow:
            indexRandom = i_cow[random.randint(0, len(i_cow) - 1)]
            number_guest_list[index], number_guest_list[indexRandom] = number_guest_list[indexRandom], number_guest_list[index]
        if index not in i_bull and index not in i_cow:
            number_guest_list[index] = str(random.randint(1, 9))
            while not isValidNumber(int(''.join(number_guest_list))):
                number_guest_list[index] = str(random.randint(1, 9))
    return int(''.join(number_guest_list))