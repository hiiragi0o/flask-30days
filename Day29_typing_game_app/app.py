# ターミナルのタイピングゲーム
import time
import random

words = ["python", "programming", "challenge", "keyboard", "game"]

print('タイピングゲームを始めます！')
time.sleep(2)

for word in random.sample(words, len(words)):
    print(f'\n次の単語をタイプしてください: {word}')
    start_time = time.time()
    user_input = input()
    end_time = time.time()

    if user_input == word:
        print(f'正解！ かかった時間: {end_time - start_time: .2f}秒')
    else:
        print('不正解...')

print('\nゲーム終了！')