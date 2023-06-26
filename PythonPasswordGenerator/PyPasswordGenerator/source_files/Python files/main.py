#takes a password length bigger than or 8, and generates a random password with random characters, numbers, and symbols
#if the length of the password is bigger than or 10, then the password generated will have more numbers than letters

upperC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
          'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowerC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

symbols = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-',
           '=', '+', '{', '[', ']', '}', "'", ';', ':', '"', ',', '<', '>', '.', '/', '?', '|']

import random




usrInpt = int(input('How long would you like your password (min 8, inclusive): '))


def generate(usrInpt):
    password = []

    dividee = 4
    res = usrInpt // dividee

    modulo = usrInpt % dividee


	for i in range(0, res + modulo):
  		randIntLetters = random.randint(0, 25)
  		password.append(lowerC[randIntLetters])

	for i in range(0, res):
  		randIntSymbols = random.randint(0, 30)
  		password.append(symbols[randIntSymbols])

	for i in range(0, res):
  		randIntNumbers = random.randint(0, 9)
  		password.append(numbers[randIntNumbers])

	for i in range(0, res):
  		randIntLetters = random.randint(0, 25)
  		password.append(upperC[randIntLetters])

    random.shuffle(password)

    password.reverse()

    finalPass = ''.join(map(str, password))

    print(finalPass)


generate(usrInpt)
