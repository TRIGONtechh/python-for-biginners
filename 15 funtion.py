def calavg(x,y):
    avg = x+y/2
    print(avg)

calavg(2,3)

# ------avg of num functions for random num----------

def calavg1(*num):
    we = 0
    for i in num:
        we= we+i
    print(we,"/",len(num),":",we/len(num))   
calavg1(1,2,3,4,5) 

# ------add of num functions----------
def caladd(*num):
    add = 0
    for i in num:
     add = add + i
    print(add)
caladd(1,2,3,5)   

    
