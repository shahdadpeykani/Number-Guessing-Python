import random

random_number = random.randint(0, 101)
print(random_number)
print("Welcome to number guessing game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty level, Type 'easy' or 'hard': ")
attempt = 0
if difficulty == "hard":
    attempt = 5
    print(f"You have {attempt} attempts.")
elif difficulty == "easy":
    attempt = 10
    print(f"You have {attempt} attempts.")
else:
    print("wrong word was entered!")

for i in range(0, attempt):
    guess = int(input("Guess a number: "))
    if guess == random_number:
        print(f"You guessed correctly! correct answer was {random_number}")
        break
    elif guess > random_number:
        print("Too high")
    else:
        print("Too low")

