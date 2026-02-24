import random

symbols = ["Moon", "Sun", "Star", "Earth", "Heaven", "Hell"]
code_length = 6
max_attempts = 10

code = random.choices(symbols, k=code_length)
attempts = 0

print(code) # For testing purposes, you can remove this line in the actual game

while attempts < max_attempts:
    raw = input(f"\nAttempt {attempts + 1}/{max_attempts}")
    guess = input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: ").strip().split()
    
    if len(guess) != code_length:
        print("The symbols blink yellow twice.")
        continue

    correct_position = sum(g == c for g, c in zip(guess, code))
    correct_symbol = sum(min(guess.count(c), code.count(c)) for c in set(code))
    incorrect = code_length - (correct_position + correct_symbol)



    print(f"{correct_position} candle ignite green")
    print(f"{correct_symbol} candle ignite blue")
    print(f"{incorrect} candle ignite red")
    

    if correct_position == code_length:
        print("The symbols along the wall rumble and glow as they individually press into the wall. One faster then the other. Once they are all sank into position, some of the candles around the room ignite with blue flames. Revealing the tapestries behind them.")
        exit()

    attempts += 1
else:
    print("The symbols blink red and reset. Roll initiative.")






#print(code)  # For testing purposes, you can remove this line in the actual game



