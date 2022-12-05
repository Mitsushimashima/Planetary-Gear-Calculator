import math

print("遊星歯車計算機")
#速度伝達比と遊星歯車の個数を入力
ratio = float(input("速度伝達比(例:3.8): "))
tolerance = float(input("速度伝達比の許容範囲: "))
number = int(input("遊星歯車の個数: "))
module = input("モジュール(指定しない場合は、そのままEnterを押してください): ")

#歯車の歯数のセットを作る
#[太陽歯車、遊星歯車、内歯車]を追加していく
gear_set = []
for i in range(15,34):
    planetary_gear = i
    for j in range(15,41):
        sun_gear = j
        for k in range(34,500):
            ring_gear = k
            if ring_gear != sun_gear + planetary_gear*2:
                continue
            if (sun_gear + ring_gear)%number!=0:
                continue
            if (planetary_gear + 2) >= (sun_gear + planetary_gear)* math.sin(math.pi/number):
                continue
            gear_set.append([j,i,k])

def diameter(module):
    if module == '':
        ans = "module × "+str(gear_set[i][2]+2)
    else:
        ans = str(float(module)*(gear_set[i][2]+2))
    return ans
            
#計算して型ごとによさそうなのを表示していく
print("以下が計算結果です。")
for i in range(len(gear_set)):
    ratio1 = (gear_set[i][2]/gear_set[i][0])+1
    if ratio-tolerance<=ratio1<=ratio+tolerance:
        print("プラネタリ型: " + str(gear_set[i])+", 外径: "+diameter(module)+"(mm), 速度伝達比: "+str(((ratio1*100)//1)/100)+"倍")
for i in range(len(gear_set)):
    ratio1 = (gear_set[i][0]/gear_set[i][2])+1
    if ratio-tolerance<=ratio1<=ratio+tolerance:
        print("ソーラ型    : " + str(gear_set[i])+", 外径: "+diameter(module)+"(mm), 速度伝達比: "+str(((ratio1*100)//1)/100)+"倍")
for i in range(len(gear_set)):
    ratio1 = gear_set[i][2]/gear_set[i][0]
    if ratio-tolerance<=ratio1<=ratio+tolerance:
        print("スター型    : " + str(gear_set[i])+", 外径: "+diameter(module)+"(mm), 速度伝達比: "+str(((-ratio1*100)//1)/100)+"倍")
print("")
print("〇〇型: [太陽歯車、遊星歯車、内歯車], 外径(mm), 速度伝達比で表示しています。")
print("外径は大体の大きさです。内歯車の太さによって変わります。")