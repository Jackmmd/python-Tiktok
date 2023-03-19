# Busqueda Binaria
lista=[2,4,6,8,10,12,14]
def busquedaBinaria(dato):
    izquierda=0
    derecha=len(lista)-1

    while izquierda <=derecha:
        medio=(izquierda+derecha)//2
        if dato==lista[medio]:
            return medio
        elif dato > lista[medio]:
            izquierda=medio+1
        else:
            derecha=medio-1
    return None

def buscar(dato):
    if busquedaBinaria(dato)==None:
        print(f'El dato {dato } No se encontro')
    else:
        print(f'El dato {dato} se encontro en la posición {busquedaBinaria(dato)}')

print('-------')
buscar(40)
print('-------')