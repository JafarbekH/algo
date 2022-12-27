def main(a,x,y):
    from math import e,sin,log 
    W2=pow((pow(e,x*y)-x*sin(a*x)-(pow(x,2)+2)/(abs(x)+5)),1/2)+pow((log((pow(x,2)+2),e)+5),1/2) 
    return round(W2,2)
print(main(0,3.66,0.75))