paises = input("Introduce los paises que quieras (separados por comas):")

lista_paises = paises.split(",")
set_paises = set({})

for pais in lista_paises:
    set_paises.add(pais.strip().capitalize())

lista_paises_ord = sorted(set_paises)
print(f'Los paises escogidos son: {", ".join(lista_paises_ord)}.')