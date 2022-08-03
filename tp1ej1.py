#1.Desarrollar una función que reciba tres números positivos y devuelva el mayor de los tres, sólo si éste es único (mayor estricto).
#En caso de no existir el mayor estricto devolver -1. No utilizar operadores lógicos (and, or, not). Desarrollar también un programa para ingresar los tres valores,
#invocar a la función y mostrar el máximo hallado, o un mensaje informativo si éste no existe


def mayor(uno,dos,tres):
    mayor = uno
    if uno>=dos:
        if uno>tres:
            mayor = uno
        elif uno==dos:
            mayor = -1
        elif tres>=uno:
            if tres==uno:
                mayor=-1
            elif tres>dos:
                mayor = tres
    elif dos>uno:
        if dos==tres:
            mayor = -1
        elif dos>tres:
            mayor = dos
        
    return mayor


print(mayor(300,200,400))

