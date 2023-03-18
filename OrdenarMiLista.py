# Ordenar mi lista
mi_list=[2,1,6,7,8,5,4,9,3]
for i in range(len(mi_list)):
    indexMin = i
    for x in range(len(mi_list)):
        if mi_list[x]<mi_list[indexMin]:
            indexMin=x
    aux=mi_list[i]
    mi_list[i]=mi_list[indexMin]
    mi_list[indexMin]=aux
    print(mi_list)
print(f'Mi lista ordenada es : {mi_list}')


