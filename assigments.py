#Takes Input from User
n=int(input("Enter Number:"))

#Converts a Number into string in order to get number of digits
a_string=str(n)
length=len(a_string)
final=0

#Logic To Find Whether Number is Armstrong Number or Not

for d in a_string:
digits=int(d)
exp=pow(digits,length)
final=final+exp
if(final==n):
print("Number is Armstrong because",final,"is Armstrong of:",n)
else:
print("Number is not Armstrong because",final,"is not Armstrong of:",n)