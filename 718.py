import random
import time

huase = ("hongtao", "fangpian", "caohua", "heitao")
shuzhi = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")


def gen():
    car = []  # 存放牌
    # 两层遁环，生成52张花色牌,生成元组
    for type in huase:
        for num in shuzhi:
            car.append((type, num))  # 元组
    car.append(("gui", "da"))
    car.append(("gui", "xiao"))
    return car


def dis(car):
    # 洗牌
    random.shuffle(car)
    random.shuffle(car)
    play1 = []
    play2 = []
    play3 = []
    dipai = 3
    for i in range(0, len(car) - dipai):
        ca=car[i]
        if i % 3== 0:     #3个人玩除以3 4个人除以4，
            play1.append(ca)
        elif i % 3 == 1:
            play2.append(ca)
        else:
            play3.append(ca)
        print(" ".join(ca), end="\t")
        time.sleep(0.1)
    print("\n")
    print("玩家1手牌", len(play1))
    for ca in play1:
        print(" ".join(ca))
    print()
    print("玩家2手牌", len(play2))
    for ca in play2:
        print(" ".join(ca))
    print()
    print("玩家3手牌", len(play3))
    for ca in play3:
        print(" ".join(ca))
    print()
    print("底牌")
    dicar = car[-3:]
    for cardd in dicar:
        print(" ".join(cardd))


car = gen()
dis(car)
