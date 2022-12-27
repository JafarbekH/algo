def main(a,x):
    from math import sin,log,cos 
    BB1=x*sin((x/2)+(x/3)+(x/4))+(log(((pow(x,2)-2)+pow(3,a)),10)/(cos(x+3)*sin(x+3)+8))
    return round(BB1,2)
print(main(2,1.46))