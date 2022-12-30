a = int(input('a='))
b = int(input('b='))
c = int(input('c='))

#kvadrat teenglamada Diskiriminant fo'rmulasini yozamiz

if b**2-4*a*c>0 :
    print(((-b-pow((b**2-4*a*c),1/2))/(2*a)) , ((-b+pow((b**2-4*a*c),1/2))/(2*a)))
else :
    print('NO')