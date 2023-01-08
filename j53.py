def main(x,y):


    if -2 <= x <= 2 and 1 <= y <= 1.5 or y >= abs(x) and y >= x :
        n = 'yes'
    else :
        n = 'no'

    return n 

print(main(0.01,0.45))