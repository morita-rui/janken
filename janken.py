import random

cnt1 = 0
cnt2 = 0
pc1 = ["グー", "チョキ", "パー"]

# ユーザーの入力
for ken in range(1, 4):
    while True:  
        pc_jan = random.choice(pc1)  
        user_jan = int(input(f'----- ラウンド {ken} -----\n1.グー 2.チョキ 3.パー\nあなたの手を選択してください。>')) - 1

        user_hand = pc1[user_jan]
        print(f'あなたの手：{user_hand}')
        print(f'コンピューターの手：{pc_jan}')

# 勝敗数





# 勝敗を判定

