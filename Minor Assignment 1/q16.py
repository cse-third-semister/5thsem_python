""" 
 16. Import relevant Python modules and print the values of eπ and πe. Then, if eπ > πe, print ”ok”.
 Otherwise print ”ok anyway”.

"""


import math
x = math.pow(math.e,math.pi)
y = math.pow(math.pi,math.e)
if(x > y):
    print("ok")

else :
    print("ok anyway")


# ok