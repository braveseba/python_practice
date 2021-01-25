numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
count_dict ={}


for x in numbers:
    if x in count_dict.keys():
        count_dict[x]+=1
    else:
        count_dict[x]=1


for key, val in count_dict.items():
    print(key, val)

