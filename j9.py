# h balandlikqan erkin tushayotgan jism qancha vaqtdan keyin yerga uriladi(g=9.8)
h=int(input("h="))


# t vaqtni tpish uchun h=g*t*t/2 dan t ni topamiz
from math import sqrt
t=sqrt((2*h)/9.8)
print(t)