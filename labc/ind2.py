import math
import sys
d = int(input("Введите год: "))
n1 = 4
n2 = 5
n3 = 6
n4 = 7
n5 = 8
n6 = 9
n7 = 10
n8 = 11
n9 = 0
n10 = 1
n11 = 2
n12 = 3
с7 = 1
с8 = 2
с9 = 3
с10 = 4
v = d % 10
if (v == n1) or (v == n2):
    s =("- Год зеленой")
elif (v == n3) or (v == n4):
    s =("- Год красной")
elif (v == n5) or (v == n6):
    s =("- Год желтой")
elif (v == с7) or (v == с8):
    s =("- Год белой")
elif (v == с9) or (v == с10):
    s =("- Год черной")
if (v == n1):
    print (d, s, "мыши")
elif (v == n2):
    print (d, s, "коровы")
elif (v == n3):
    print (d, s, "тигра")
elif (v == n4):
    print (d, s, "зайца")
elif (v== n5):
    print (d, s, "дракона")
elif (v== n6):
    print (d, s, "змеи")
elif (v == n7):
    print (d, s, "лошади")
elif (v == n8):
    print (d, s, "овцы")
elif (v == n9):
    print (d, s, "обезьяны")
elif (v == n10):
    print (d, s, "курицы")
elif (v == n11):
    print (d, s, "собаки")
elif (v == n12):
    print (d, s, "свиньи")