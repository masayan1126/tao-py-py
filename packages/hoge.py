# 文字列の近似値

string1 = "lemon"
string2 = "almne"

result = 0

for st in string1:
    if st in string1 and string1.find(st) == string2.find(st):
        result += 1
        print(st)

length = len(string1)
