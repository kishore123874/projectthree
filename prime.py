n=9
m=int(n/2)
# print(m)
if n>1:
    for i in range(2,m+1):
        if(n%i==0):
            print(n,"is nor prime")
            break
    else:
         print(n,"is a prime")
else:
    print(n,"not a prime")
