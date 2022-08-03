#desarrollar una función que reciba tres números enteros positivos y verifique si corresponden a una fecha gregoriana válida (día, mes, año).
#Devolver True o False según la fecha sea correcta o no. Realizar también un programa para verificar el comportamiento de la función.



def fecha(dia,mes,año):
    if dia<31 and dia>0:
        if mes<13 and mes>0:
            if año<2023 and año>0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
print(fecha(30,3,1900))
