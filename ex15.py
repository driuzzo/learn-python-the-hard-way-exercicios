from sys import argv

# argv recebe script e filename
script, filename = argv

# variável que abre um arquivo
txt = open(filename)

# printa o conteúdo do arquivo
print(f"Here is your file {filename}:")
print(txt.read())

# pede para digitar novamente o nome do arquivo
print("Type the filename again:")
file_again = input("> ")

# variável para abrir novamente o arquivo
txt_again = open(file_again)

# printa novamente o conteúdo do arquivo
print(txt_again.read())