def main(b,a,c,d,x):
    from math import cos
    y2=((a*pow(x,2)+b*x+c)/(x*pow(a,3)+pow(a,2)+pow(a,(b-c))))+cos(abs((a*x+b)/(c*x+d+pow(2,c))))
    return round(y2,2)
print(main(0,0,1,1,0.12))