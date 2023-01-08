def main(x,y):


    if -1 <= x <= 1 and -1 <= y <= 0.5 and y <=x/2  :
        n = 'yes'
    else :
        n = 'no'

    return n 

print(main(-0.43,0.26))