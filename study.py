example1 = "sometimes waht you say is less important than how you say it"
print(type(example1))
example2= "71"
print(type(example2))
example3= 71
print(type(example3))
example4= 71.0
print(type(example4))
example5 = 3.14j
print(type(example5))
example6= True
print(type(example6))
p = 3.14
s =str(p)
print(type(s))
f = 3.14
i = int(f)
print(i, '\n')
print(type(i))
i = 3
f = float(i)
print (f,'\n')
print(type(f))
x = 39
v = "11"
y = "2.5"
z = "I am at_"
print(x-int(v))
print(x-float(y))
print(z+str(x))
a = 36.5
b = '30'
c = '3.5'
d = ' F is enough for room temperature.'
print(str(a+int(b)+float(c))+d)
a = 5
b = 4 
print (a, b,sep=":)")

def ArmStrong(n):
x=n # Backup of the Input Number
S=0 # This is used to doing the Summation
print("Input Number is : ",n)
l=len(str(n)) # Find length of Number by Converting to String first
while(x !=0):
a=x%10 # Take one number at a time
S=S+pow(a,l) # Calculation
x=x//10 # breaking the number so that it gives the next number in Iteration

if (S==n): # Checking whether Number is ArmStrong
print ("Input is an Armstrong number ",(n))
else:
print ("Input is Not an Armstrong number ", (n))