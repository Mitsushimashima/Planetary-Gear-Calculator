import math

print("遊星歯車計算機")
#速度伝達比と遊星歯車の個数を入力
ratio = float(input("速度伝達比(例:3.8): "))
tolerance = float(input("速度伝達比の許容範囲: "))
number = int(input("遊星歯車の個数: "))

solar_gear = 15
planetary_gear = 15
internal_gear = 34

#歯車の歯数のセットを作る
#[太陽歯車、遊星歯車、内歯車]を追加していく
gear_set = []
for i in range(15,34):
    planetary_gear = i
    for j in range(15,41):
        solar_gear = j
        for k in range(34,100):
            internal_gear = k
            if internal_gear != solar_gear + planetary_gear*2:
                continue
            if (solar_gear + internal_gear)%number!=0:
                continue
            if (planetary_gear + 2) >= (solar_gear + planetary_gear)* math.sin(180/number):
                continue
            gear_set.append([j,i,k])

#許容範囲以内ならリストに加える
print("以下が計算結果です。")
print("プラネタリ型")
for i in range(len(gear_set)):
    ratio1 = (gear_set[i][2]/gear_set[i][0])+1
    if ratio-tolerance<=ratio1<=ratio+tolerance:
        print(str(gear_set[i])+":"+str(ratio1)+"倍")
print("ソーラ型")
for i in range(len(gear_set)):
    ratio1 = (gear_set[i][0]/gear_set[i][2])+1
    if ratio-tolerance<=ratio1<=ratio+tolerance:
        print(str(gear_set[i])+":"+str(ratio1)+"倍")
print("スター型")
for i in range(len(gear_set)):
    ratio1 = gear_set[i][2]/gear_set[i][0]
    if ratio-tolerance<=ratio1<=ratio+tolerance:
        print(str(gear_set[i])+":"+str(-ratio1)+"倍")
print("[太陽歯車、遊星歯車、内歯車]:速度伝達比で表示しています。")