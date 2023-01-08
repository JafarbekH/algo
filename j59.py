def main(x,y):


    if -0.5 <= x <= 0.5 and -1 <= y <= 1 and y == 2*x+1 and y == -2*x+1 and y == -2*x-1 and y == 2*x-1  :
        n = 'yes'
    else :
        n = 'no'

    return n 

print(main(0.77,0.32))