

def sumatoria(numero1,numero2):
    resultado_suma=numero1 + numero2
    return resultado_suma

def restar(numero1,numero2):
    resultado_resta=numero1 - numero2
    return resultado_resta

def multiplicar(numero1,numero2):
    resultado_multiplicacion=numero1*numero2
    return resultado_multiplicacion

def dividir(numero1, numero2):
    if numero2==0:
        return "error: no se puede dividir por cero"
    else:
        resultado_division=numero1/numero2
        return resultado_division