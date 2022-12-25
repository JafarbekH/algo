def main(a,b,c,x):
    from math import cos, sqrt
    w1=0.75+(8.2*pow(x,2)+sqrt(abs(pow(x,3)+3*x)+cos(x-2)))/((a/4)+(b/3)+(c/2)+1)
    return round(w1,2)
print(main(1,1,1,0.33))