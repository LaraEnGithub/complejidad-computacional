import random

'''
Clase para modelar graficas y resolver de manera no determinista
el problema de alcanzabilidad.
'''


'''
Generdor aleatorio de ejemplares para el problema de alcanzabilidad:
Regresa una grafica, representada mediante su matriz de adyacencia
Regresa dos vertices aleatorios de la grafica: s, t
''' 
def generar_matriz_adyacencia():
    n = random.randint(10, 20)
    matriz = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            valor = random.randint(0, 1)
            matriz[i][j] = valor
            matriz[j][i] = valor

    vertice_s, vertice_t = random.sample(range(n), 2)

    return matriz, (vertice_s, vertice_t)


'''
Fase adivinadora:
Genera una secuencia aleatoria de vertices con 
longitud de la secuencia se eligida al azar entre 1 y n, 
donde n es el tamaño de la grafica. 
'''
def generar_camino(matriz):
    n = len(matriz)
    longitud = random.randint(1, n)
    camino = [random.randrange(n) for _ in range(longitud)]

    return camino


'''
Fase verificadora:
Verifica que una secuencia de vertices sea un camino valido de s a t:
1. El primer y el ultimo vertice de la secuencia deben ser s y t.
2. Cada arista consecutiva inducida por la secuencia debe existir
   en la matriz de adyacencia.
3. Ningun vertice debe repetirse dentro de la secuencia.
'''
def verificar_camino(matriz, camino, s, t):
    if camino[0] != s or camino[-1] != t:
        return False

    for i in range(len(camino) - 1):
        actual, siguiente = camino[i], camino[i + 1]
        if matriz[actual][siguiente] == 0:
            return False

    if len(set(camino)) != len(camino):
        return False

    return True


# Impresion en pantalla de la matriz de adyacencia
def imprimir_matriz(matriz):
    n = len(matriz)
    print(f"\nNumero de vertices: {n}\n")

    encabezado = "    " + " ".join(f"{j:2d}" for j in range(n))
    print(encabezado)

    for i, fila in enumerate(matriz):
        print(f"{i:2d}: " + " ".join(f"{valor:2d}" for valor in fila))


def main():
    matriz, (vertice_s, vertice_t) = generar_matriz_adyacencia()
    imprimir_matriz(matriz)
    print(f"\nVertices seleccionados: s={vertice_s}, t={vertice_t}")

    camino = generar_camino(matriz)
    print(f"Camino aleatorio: {camino}")

    es_valido = verificar_camino(matriz, camino, vertice_s, vertice_t)
    print(f"Es un camino valido y sin repeticiones de s a t: {es_valido}\n")


if __name__ == "__main__":
    main()
