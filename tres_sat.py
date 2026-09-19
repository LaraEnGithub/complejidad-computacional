import random

'''
Clase para modelar clausulas de tres variables y resolver
de manera no determinista el problema de 3SAT
'''

# Las variables tienen nombres x, y, z
def generar_nombres(n):
    letras = ['x', 'y', 'z']
    return [f"{letras[i % 3]}{i // 3 + 1}" for i in range(n)]

'''
Generador aleatorio de ejemplares para el problema 3SAT
'''
def generar_ejemplar_3sat():
    n = random.randint(10, 50)
    m = random.randint(5, 25)
    nombres = generar_nombres(n)

    clausulas = []
    for _ in range(m):
        variables = random.sample(range(n), 3)
        clausula = [(v, random.choice([True, False])) for v in variables]
        clausulas.append(clausula)

    return nombres, clausulas

# Imprime el ejemplar de 3SAT en pantalla
def imprimir_ejemplar(nombres, clausulas):
    print(f"\nNumero de variables: {len(nombres)}")
    print(f"Numero de clausulas: {len(clausulas)}\n")

    for clausula in clausulas:
        literales = [f"~{nombres[v]}" if neg else nombres[v] for v, neg in clausula]
        print("(" + " v ".join(literales) + ")")


'''
Fase adivinadora:
Genera de forma aleatoria una asignacion para las variables del ejemplar
'''
def generar_asignacion(n):
    return [random.choice([True, False]) for _ in range(n)]


def imprimir_asignacion(nombres, asignacion):
    print("\nAsignacion de variables:")
    for nombre, valor in zip(nombres, asignacion):
        print(f"{nombre} = {valor}")

'''
Fase verificadora:
Verifica que una asignacion dada satisface un ejemplar
'''
def verificar_asignacion(clausulas, asignacion):
    for clausula in clausulas:
        satisfecha = False
        for v, neg in clausula:
            valor = not asignacion[v] if neg else asignacion[v]
            if valor:
                satisfecha = True
                break
        if not satisfecha:
            return False

    return True


def main():
    nombres, clausulas = generar_ejemplar_3sat()
    imprimir_ejemplar(nombres, clausulas)

    asignacion = generar_asignacion(len(nombres))
    imprimir_asignacion(nombres, asignacion)

    es_satisfactible = verificar_asignacion(clausulas, asignacion)
    print(f"\n{'Verdadero' if es_satisfactible else 'Falso'}\n")


if __name__ == "__main__":
    main()
