secret_number = 4

guess = int(input("Guess a number from 1 to 9: "))

while guess != secret_number:
    guess = int(input("Guess a number from 1 to 9: "))

print("Bravo!")
