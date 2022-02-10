secret_number = 1
tries = 3

print("GUESS THE SECRET NUMBER" + "!" * secret_number)
print(f"{tries} tries left")
guess = int(input("Guess a number from 0 to 9: "))

while guess != secret_number and tries > 1:
    tries -= 1
    print(f"{tries} left")
    guess = int(input("Guess a number from 0 to 9: "))

if guess == secret_number:
    print("Bravo!")
else:
    print(f"Loser! It was {secret_number}")
