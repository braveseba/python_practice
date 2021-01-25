'''example_1 = "sometimes wat you say is less important tan ow you say it"
print(type(example_1))
example_2 = "71"
print(type(example_2))
example_3 = 71
print(type(example_3))
example_5 = 71.0
print(type(example_5))
example_6 = 3.14j
print(type(example_6))
example_7 = True #  Note that we write the first letter of True in uppercase
print(type(example_7))
x = 39
y = "11"
z = "I am at_"
v ="11"
print(x-int(v))
print(x-float(y))
print(z+str(x))
a = 36.5
b = '30'
c = '3.5'
d = ' F is enough for room temperature.'

print(str(a+int(b)+float(c))+d)

color = 'red'  # str type variable
season = 'summer'
price = 250  # int type variable
pi = 3.14  # float type variable
color = 'blue'  # You can always assign a new value to a created variable
price = 100  # value of 'price' is changed
season = 'winter' 
a = 5
b = 55
c = 555
c = a
b = c
a = b 
logic = True and False or not False or False
print(logic)

print(color, price, season, sep=':)')
name = "Sebahat"
last_name = "Karaarslan"
output = f'Hello,{name} {last_name}'
print(output)
days_of_feb = 28


print("it\'s very important")
print(1 or 2)
print(1 and 2) 
print (1 or None)
print(True or False)
print(False and True)
print(True and False or True)
no1, no2 = 46, 52
no3 = no1 -no2
print(no3)
no1 = 46
print(no1/23)
print((3 * 4)/2)
print(7//2)
print(3**2) 
number = 2020
text = "cilderen deserve respect as muc as adult in"
print(text,number)
print("yesterday I ate " ,2 , "apples")
print("i", end= ' ')
print('will say', end =' ')
print("I missed you ", end= ' ')
print('to my mother')
print('smoking', 'is', 'slowly', 'killing me', sep=' + ')
'hello'
3.14
74
print(type('hello'))
city = 'Phoenix'
print(city[1:])  # starts from index 1 to the end
print(city[:6])  # starts from zero to 5th index
print(city[::2])  # starts from zero to end by 2 step
print(city[1::2])  # starts from index 1 to the end by 2 step
print(city[-3:])  # starts from index -3 to the end
print(city[::-1])  # negative step starts from the end to zero

abc = 'Python Language'
print(abc[:4])
print(abc[:1])
print("clarus"+"way")
print(3*'no way!')
fruit = 'Orange'
vegetable = 'Tomato'
print("using + :", fruit + vegetable)
print("using * :", 3 * fruit)
fruit = 'orange'
fruit += ' apple'
fruit += ' banana'
fruit += ' apricot'

print(fruit)

abc = "Orange"
cdb = "Tomato"
amount = 6
output =f"The amount of {abc} and {cdb} we bougt are totally {amount} pounds"
number= "32"
number_2 = 1988
number_3 = int(number) + int(number_2)
x = False
y = not x
print("{4} {9} {1} {7} {5} {0} {6} {8} {3} {2}".format('while', 'dream', 'work.', 'and', 'Some', 'success', 'others', 'of', 'wake up', 'people'))
print(float("140" * int(input("Enter a number:" ))'''
'''actual_cost = float(input("please enter a actual product price:"))
sale_amount = float(input(please enter the price of sales:" ))

if(actual_cost - sale_amount >0):
    amount = actual_cost - sale_amount''''

# Python Program to Calculate Profit or Loss
 
actual_cost = 31.87
sale_amount = 45.00
if(actual_cost > sale_amount):
    amount = actual_cost - sale_amount
    print("Total Loss Amount = {0}".format(amount))
elif(sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total Profit = {0}".format(amount))
else:
    print("No Profit No Loss")

