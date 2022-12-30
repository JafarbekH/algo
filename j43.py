x = float(input('x='))
y = float(input('y='))

if x<0 and y<0 :
    print(abs(x), abs(y))
if x<0 and y>0 or x>0 and y<0 :
    print(x/2, y/2 )
if x>0 and y>0 :
    print(x , y)