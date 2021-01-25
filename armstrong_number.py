num=num=int(input("Enter a number:"))
temp=num
sum=0
length=len(str(num))
for i in range(length):
    rem=temp%10
    temp=temp//10
    sum=sum+pow(rem,length)
if(sum==num):
   print(num," is a Armstrong number")
else:
   print(num," is not a Armstrong number")