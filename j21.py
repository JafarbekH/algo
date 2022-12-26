def main(a,b):
    T=pow(a,1/5)+pow(((a+b)*b)/(2*b+a*b),1/4)*(pow(a,2)+pow(b,2)+2)
    return round(T,2)
print(main(0.36,1.02))