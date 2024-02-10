import random
import steps
from steps import *

card=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
random_card_index=random.sample(range(len(card)),4)
random_card_up=[]
while(steps.not_diff(random_card_index)):
    random_card_index = random.sample(range(len(card)), 4)
for index in random_card_index:
    random_card_up.append(card[index])
#随机打乱
random.shuffle(random_card_up)
random_card_down=random_card_up.copy()
#撕碎后的卡牌
for i in range(len(random_card_up)):
    random_card_up[i] = random_card_up[i] + '_up'
for i in range(len(random_card_down)):
    random_card_down[i] = random_card_down[i] + '_down'
random_card=random_card_up+random_card_down
name=input("请输入你的名字：")
for i in range(len(name)):
    random_card=steps.shuffle_card(random_card)
random_card=steps.insert_list(random_card)
#上一半卡片藏起来
first_half_card=random_card[0]
print(f"藏起来的卡片为：{first_half_card}")
del random_card[0]
where=input("你是南方人还是北方人？输入：南方，北方，不知道：")
if where=="南方":
    random_card=steps.insert_list(random_card,number=1)
elif where=="北方":
    random_card=steps.insert_list(random_card,number=2)
elif where=="不知道":
    random_card=steps.insert_list(random_card,number=3)

sex=input("你是男生还是女生？输入：男生，女生：")
if sex=="男生":
    del random_card[0]
elif sex=="女生":
    del random_card[0]
    del random_card[1]
print("****见证奇迹的时刻****")
for i in range(7):
    random_card=shuffle_card(random_card)

last_half_card=steps.throw_bad_things(random_card)
your_number=steps.examine(first_half_card,last_half_card)
if(your_number!=0):
    print(your_number)
    print("龙年大吉")
else:
    print("你输了")


