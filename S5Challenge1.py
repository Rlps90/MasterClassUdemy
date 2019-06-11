#Coding challenge 1
#Divisao de 2 numeros sem travar o programa
try:
    def division(a, b):
        return a/b
    result = division(10, 2)
    print(result)

except ZeroDivisionError:
    print("Nao eh possivel dividir por zero.")

finally:
    print("Fim do programa.")




