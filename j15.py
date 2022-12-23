def umumiy_qarshilik(R1,R2,R3):
    #Izoh o'rnida aytib ketish joizki Rum umumiy qarshilikni ifoadalaydi
    Rum=1/(1/R1+1/R2+1/R3) 
    return round(Rum,2) 
print(umumiy_qarshilik(1,7,3))