def funksiya(x,y):
    from math import e, atan, cos
    f2=(((1/(x+(2/pow(x,2))+3/pow(x,3)))+pow(e,(pow(x,2)+3*x)))/(atan(x+y)+pow(abs(5+x),2)))-pow(cos(pow(y,2)+pow(x,2)/2),2) 
    return round(f2,2) 
print(funksiya(3.19,4.75))