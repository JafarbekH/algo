def main(x,y):


    if -1 <= x <= 1 and -1 <= y <= 1 and pow(x,2) + pow(y,2) <=1 :
        n = 'yes'
    else :
        n = 'no'

    return n 

print(main(-0.32,1.07))