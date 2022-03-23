from game_Bull_Cow.scripts.validNumber import isValidNumber
from game_Bull_Cow.scripts.checkForCowBull import checkCowBull
from game_Bull_Cow.scripts.gameAlgorithm import gameAI
import random

numberForGuess = 0
numberOfComputer = 0
countOfTry = 0
index_cow = []
index_bull = []

while not isValidNumber(numberForGuess):
    numberForGuess = random.randint(1000, 9999)
while not isValidNumber(numberOfComputer):
    numberOfComputer = random.randint(1000, 9999)

index_cow, index_bull = checkCowBull(numberForGuess, numberOfComputer)

while len(index_bull) != 4:
    numberForGuess = gameAI(numberForGuess, index_cow, index_bull)
    index_cow, index_bull = checkCowBull(numberForGuess, numberOfComputer)
    countOfTry += 1
    print(f"Попытка: {countOfTry}; Число: {numberForGuess}; Число, которое нужно отгадать: {numberOfComputer}")