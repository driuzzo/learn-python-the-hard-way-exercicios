#tipos de pessoa recebe 10 e cria uma variável x que recebe uma string dizendo que existe x tipos de pessoa, utilizando a vairável tipos de pessoa
types_of_people = 10
x = f"There are {types_of_people} types of people."
# binário recebe binário e não recebe não. y recebe uma string com um texto que chama as duas variáveis
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"
#printa as duas frases acima (x e y)
print(x)
print(y)
#repete x e y
print(f"I said: {x}")
print(f"I also said: '{y}'")
# hilário recebe falso. joke_evaluation recebe uma string perguntando se é engraçado
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
# printa joke_evaluation e chama hilarious também
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
