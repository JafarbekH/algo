a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
d = float(input('d='))

if a<=b<=c<=d :
    print(d, d, d, d)
if  a<b and a<c and a<d:
    print(a, a, a, a)
if  b<a and b<c and b<d:
    print(b, b, b, b)
if  d<a and d<c and d<b:
    print(d, d, d, d)
if  c<a and b>c and c<d:
    print(c ,c ,c ,c)