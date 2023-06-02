#%% 로또 번호 만들기
# - 범위 : 1~45
# - 숫자 : 6개
# - 같은 숫자 존재 불가능
import random

# LottoNum : 로또 번호(최종 6개)
lottoNum = []

for i in range(1,7):
    while True :
        # pickNum : 단일 번호
        pickNum = random.randrange(1,46)
        if pickNum in lottoNum:
            continue
        else:
            lottoNum.append(pickNum)
            break

print("로또번호")
print(lottoNum)