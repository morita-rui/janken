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
        
        if user_hand == pc_jan:
            print("引き分けです")
            continue
        elif (user_hand == "グー" and pc_jan == "チョキ") or \
             (user_hand == "チョキ" and pc_jan == "パー") or \
             (user_hand == "パー" and pc_jan == "グー"):
            print("あなたの勝ちです")
            cnt2 += 1
            break  
        else:
            print("コンピューターの勝ちです")
            cnt1 += 1
            break  

# 勝敗数

print(f'あなた：{cnt2}勝')
print(f'コンピューター：{cnt1}勝')


# 勝敗を判定
if cnt2 > cnt1:
    print('あなたの総合勝利です！')
elif cnt2 < cnt1:
    print('コンピューターの総合勝利です！')
else:
    print('引き分けです！')

    