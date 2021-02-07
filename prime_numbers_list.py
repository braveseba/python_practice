start = 1
end = 100
liste= []
  
for i in range(start, end+1): 
  if i>1: 
    for j in range(2,i): 
        if(i % j==0): 
            break
    else: 
        liste.append(i)
        
print(liste)