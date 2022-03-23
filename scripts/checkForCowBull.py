def checkCowBull(number_guess, number_computer):
    i_cow, i_bull = [], []
    try:
        number_guess_list = list(str(number_guess))
        number_computer_list = list(str(number_computer))
        for index in range(len(number_guess_list)):
            if number_computer_list[index] == number_guess_list[index]:
                i_bull.append(index)
            elif number_guess_list[index] in number_computer_list:
                i_cow.append(index)
        return i_cow, i_bull
    except:
        return i_cow, i_bull