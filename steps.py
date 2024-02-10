import random

def not_diff(card_index_list):
    return len(card_index_list) != len(set(card_index_list))
def shuffle_card(card_list):
    card_list.append(card_list[0])
    del card_list[0]
    return card_list

def insert_list(card_list,number=3):
    first_three=card_list[:number]
    rest_of_the_list=card_list[number:]
    random_index = random.randint(1, len(rest_of_the_list) - 1)
    # 在计算出的随机位置插入之前取出的三个元素
    for i in range(number):
        rest_of_the_list.insert(random_index + i, first_three[i])
    return rest_of_the_list

def throw_bad_things(card_list):
    print("好运留下来，烦恼丢出去")
    shuffle_card(card_list)
    del card_list[0]
    if(len(card_list)!=1):
        throw_bad_things(card_list)
    return card_list

def examine(first_half_card,last_half_card_list):
    card_num_up=first_half_card.split('_')[0]
    card_num_down=last_half_card_list[0].split('_')[0]
    if card_num_up==card_num_down:
        return card_num_up
    else:
        return 0