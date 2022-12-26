def main(x1,x2,c,d):
    from math import tan, sqrt, sin
    F=abs(pow(sin(abs(c*pow(x2,3)+d*pow(x1,3)-c*d)),2)/sqrt(c*pow(x1,2)+d*pow(x2,2)+5)+2)+tan(x1*pow(x2,2+pow(d,3)))
    return round(F,2)
print(main(4.01,0.33,0,1))