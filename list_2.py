'''gracer = True
minced =  True
lettuce = True
onion = True
bread = True
grocer = True

hamburger = minced and grocer and bread and (lettuce or onion)
print(hamburger)
if hamburger:
    print("Bon Apetito")
    if 1 :
        print("I will be exuceted")
if "0": 
    print( "I will not")'''

s = "Clarusway"

# Let’s remove the character at index 3 in above created string object i.e.
 n = 3
# Slice string to remove character at index 3
if len(s) > n:
    s = s[0 : n : ] + s[n + 1 : :]