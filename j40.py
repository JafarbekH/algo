a = int(input('a='))
b = int(input('b='))
c = int(input('c='))

if a>0 and b<0 and c<0 :
    print(a**2, b, c)
if a>0 and b>0 and c<0 :
    print(a**2, b**2, c)
if a>0 and b>0 and c>0 :
    print(a**2, b**2, c**2)
if a<0 and b<0 and c<0 :
    print(a, b, c)
if a>0 and b<0 and c>0 :
    print(a**2, b, c**2)
if a<0 and b>0 and c>0 :
    print(a, b**2, c**2)
if a<0 and b<0 and c>0 :
    print(a, b, c**2)
if a>0 and b>0 and c<0 :
    print(a**2, b**2, c)