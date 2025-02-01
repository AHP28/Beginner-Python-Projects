##Collatz
import time
i= int(input())
l= [i]
o= []
while i!=1:
    if i%2==0:
        i = i//2
        l.append(i)
    else:
        i = 3*i+1
        l.append(i)

for k in l:
    o.append(k)
    if o[len(o)-1]==1:
        print(k)
    else:
        print(k, end=", ")