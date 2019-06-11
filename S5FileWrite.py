#escrevendo e lendo conteudo de outro arquivo
file = open("demo.txt", 'w')
file.write("Testando salvar info no demo.txt\n")
file.close()

file = open("demo.txt", 'r')
content = file.read()
print(content)
file.close()

#append pra nao perder o que foi escrito anteriormente
file = open("demo.txt", 'a')
file.write("Cuzao")
file.close()

file = open("demo.txt", 'r')
content = file.read()
print(content)
file.close()

