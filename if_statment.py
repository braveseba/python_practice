'''max
set_1 = {"red", "blue", "pink" , "red"
colors = "red", "blue","pink", "red"
set_2= colors}
print(set_2)'''
letter = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split()
print(set(letter))
flower_list = ['rose', 'violet', 'carnation', 'rose', 'orchid', 'rose', 'orchid']
flowerset = set(flower_list)
flowerlist = list(flowerset)
print(flowerset)
print(flowerlist)
grocer = ["banana", ["orange", ["apple", "eggplant", "melon", "spinach", "cheese", "leek" ], "water"], "mandarin"]
print(grocer[1][1][1::2])
x=grocer.popitem()
print(x)


