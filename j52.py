def main(x,y):

    if -2 <= x <= 1 and -1 <= y <= 1 and y == abs(x) and y == ((2*x)/3)+1/3 and y == (x/3)-1/3 :
        n = print('yes')
    else :
        n = print('no') 
    return n
print(main(0.11,0.25))