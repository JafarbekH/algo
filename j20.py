def main(x,y):
    from math import sin, cos
    T11=((pow(x,2)+1)/pow(x,2)+(x*y+pow(y,2))/((pow(y,2)+(y+x*y)/(abs(x*y)+5)))+1/(1+cos(x)+1/sin(abs(x))))
    return round(T11,2)
print(main(7.09,3.92))