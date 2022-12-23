def funksiya(x,y):
    from math import tan, cos, log, pi
    f1=((2*tan(x+pi/6))/((1/3)+pow(cos(y+pow(x,2)),2)))+log(2,pow(x,2)+2) 
    return round(f1,2) 
print(funksiya(1.7,5.18))