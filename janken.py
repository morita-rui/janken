import random

cnt1 = 0
cnt2 = 0
pc1 = ["グー", "チョキ", "パー"]

# ユーザーの入力





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