 import sys
from random import randint

try:
    d = open("Warenkorb.txt", "w")
except:
    print("Oh my days")

warenkorb = []

for x in range(0, 12):
    i = randint(0, 100)
    warenkorb.append(i)


f = len(warenkorb)
r = str(warenkorb)
t = -1
for i in range(0, f):
    t += 1
    d.write(str(warenkorb[t])+"\n")




print(f)
d.close()