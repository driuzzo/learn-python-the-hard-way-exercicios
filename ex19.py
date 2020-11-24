# cria a função com dois argumentos e printa os dois depois
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man, that's enough for a party!")
    print("Get a blanket.\n")

# aqui printa um texto antes e chama a função passando os valores para cada argumento, 20 para queijo e 30 para bolacha
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# aqui cria duas variáveis antes para serem usadas como argumentos na função
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# aqui chama a função usando cálculo como argumentos
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 50 + 6)

# aqui chama a função usando variável + cálculo como argumento
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)