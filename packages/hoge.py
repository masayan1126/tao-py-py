
int_array =[1,2,3,4,5,6,7,8,9,10]

# 何個ずつに分割するか
n=4

# リスト内包表記
# rangeの第3引数(step)に数値を指定すると、stepずつ増加する等差数列が生成される([0, 4, 8]の1つずつがiに入る)
splited = [int_array[i: i+n] for i in range(0, len(int_array), n)]

print(splited) # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]]
