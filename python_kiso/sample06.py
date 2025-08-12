# number_game.py

import random


secret = random.randint(1,10)
guess = int(input("1～10の数字を当ててください："))

if guess == secret:
    print("正解です")

else:
    print("間違えです。正解は",secret,"です")