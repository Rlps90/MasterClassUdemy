#abrir arquivo, ler e escrever informacoes
file = open("demo.txt", 'w')
file.write("Leonardo otario.\n")
file.close()

file = open("demo.txt", 'r')
print(file.read())
file.close()

file = open("demo.txt", 'a')
file.write("Leonardo otario.\n")
file.close()

