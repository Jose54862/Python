#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
ingredientes = ["mozzarella", "tomate"]
pizza = input("¡Bienvenido a la pizzeria Bella Napoli! ¿Quiere una pizza vegetariana?: ").lower()
if pizza == "si":
    pizza = "es vegetariana"
    ingrediente_vegetariano = input("Elija un ingrediente: tofu o pimiento: ").lower()
    if ingrediente_vegetariano == "tofu" or  ingrediente_vegetariano == "pimiento":
        ingredientes.append(ingrediente_vegetariano)
        print(f"Su pizza {pizza} y contiene: {", ".join(ingredientes)}.")
    else:
        print("Por favor elija uno de los dos ingredientes.")
elif pizza == "no":
    pizza = "no es vegetariana"
    ingrediente_no_vegetariano = input("Elija un ingrediente: peperoni, jamon o salmon: ").lower()
    if ingrediente_no_vegetariano == "peperoni" or ingrediente_no_vegetariano == "jamon" or ingrediente_no_vegetariano == "salmon":
        ingredientes.append(ingrediente_no_vegetariano)
        print(f"Su pizza {pizza} y contiene: {", ".join(ingredientes)}.")
    else:
        print("Por favor elija uno de los ingredientes disponibles.")
else:
    print("Por favor responda con si/no")