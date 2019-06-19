aa =[1,2,4,"d",'d','2','2']
cont_dict = dict()
for i in aa:
    if i in cont_dict:
        cont_dict[i]+= 1
    else:
        cont_dict[i]= 1

print(cont_dict[1])
# cc =[1,2,4,"d",'d','2','2']
# print(list(set(cc)))


