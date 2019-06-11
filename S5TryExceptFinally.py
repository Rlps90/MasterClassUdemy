#usar quando tiver uma excecao no programa
try:
    a = 20
    b = 2
    print(a/b)

except ZeroDivisionError:
    print("Nao eh possivel dividir por zero.")

finally:
    print('Isto sera executado de qualquer jeito')