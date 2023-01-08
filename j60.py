def main(x,y):


    if -2 <= x <= 0 and -1 <= y <= 1 and y == x/2+1 and y == -x/2-1 or 0 <= x <=1 and -1 <= y <= 1 and pow(x,2)+pow(y,2)<= 1 :
        n = 'yes'
    else :
        n = 'no'

    return n 

print(main(0.7,0.12))