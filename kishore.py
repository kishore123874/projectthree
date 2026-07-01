a=int(input("Enter a number:"))
i=0
rev=0
while(i<a):
    rem=a%10
    rev=rev*10+rem
    a=a//10
print(rev)
  
