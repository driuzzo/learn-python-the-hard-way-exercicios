#carros recebe 100
cars = 100
#espaço no carro receve 4.0
space_in_a_car = 4.0
#motoristas recebe 30
drivers = 30
#passageiros recebe 90
passengers = 90
#carros não dirigidos recebe carros menos motoristas
cars_not_driven = cars - drivers
#carros dirigidos recebe motoristas
cars_driven = drivers
#capacidade de carona recebe carros dirigidos vezes o espaço no carro
carpool_capacity = cars_driven * space_in_a_car
#média de passageiros por carro recebe passageiros dividido por carros dirigidos
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
