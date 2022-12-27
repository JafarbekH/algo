def main(x,y,z):
    from math import e,sin 
    AF=pow(2,-x)*pow((x+pow((abs(y)+20),1/4)),1/2)*pow(((pow(e,x-1)/sin(z+2))+2),1/3)
    return round(AF,2)
print(main(1,1.84,0.53))