def aka(x):
    from math import tan,sin,cos 
    AA=pow((2*tan(x+2)-cos(x+pow(2,x)))/(1+pow(cos(x+2),2)),1/2)+sin(pow(x,2))/(pow(x,2)+3)
    return round(AA,2)
print(aka(8.2))