def main(x,y):


    if -1 <= x <= 1 and -1 <= y <= 1 and pow(x,2) + pow(y,2) <=1 and pow(x,2) + pow(y,2) >= 0.5 :
        n = 'yes'
    else :
        n = 'no'

    return n 

print(main(0.3,0.49))

print(pow(0.3,2)+pow(0,49,2))