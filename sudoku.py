from pprint import pprint
# Para imprimir de forma bonita la salida del sudoku

def encontrar_hueco(puzle):
    # Encontrar la siguiente fila o columna que no está rellena aun y que
    # esta representada con un -1
    # Devolver una tupla formada por el indice de esa fila, columna (o (None, None) si no existe
    # ningún hueco.

    # Ten en cuenta que un sudoku tiene 9 filas y 9 columnas con lo que la posicion de cada fila
    # y columna ira desde el (0.....8)
    for f in range(9):
        for c in range(9):  # range 9 es (0,1,2,3....8)
            if puzle[f][c] == -1:
                return f, c

    return None, None  # Si no existen huecos en el puzle que podamos cambiar.


def es_valido(puzle, eleccion, fila, columna):
    # Verificar que la elección del numero para la fila/columan es válida
    # Devolver True si lo es y False en caso contrario. Para ello tenemos que realizar
    # las siguientes comprobaciones:

    # Empecemos por comprobar las filas (no se pueden repetir los numeros del 1 - 9)
    fila_valores = puzle[fila]
    if eleccion in fila_valores:
        return False

    # Continuamos con las columnas.(Tampoco se pueden repetir los numeros del 1 - 9)
    # col_valores=[]
    # for i in range(9):
    #     col_valores.append(puzle[i][columna])
    col_valores = [puzle[i][columna] for i in range(9)]
    if eleccion in col_valores:
        return False

    # Terminamos comprobando que tampoco se repitan los numeros del 1 - 9  en el cuadrado
    # de 3 x 3 corresondiente.
    # Necesitamos saber donde comienza el cuadrado de 3 x 3 (sus cordenadas) e iterar
    # sobre los valores de cada fila/columna.
    fila_inicio = (fila // 3) * 3  # 1 // 3 = 0 ; 5 // 3 = 1, ...
    col_inicio = (columna // 3) * 3

    for f in range(fila_inicio, fila_inicio+3):
        for c in range(col_inicio, col_inicio + 3):
            if puzle[f][c] == eleccion:
                return False

    # Si hemos llegado hasta este punto del código es que todas las comprobaciones esta ok y el
    # valor de elección es válido
    return True


def resolver_sudoku(puzle):
    # resolver un sudoku utilizando iteraciones
    # El argumento puzzle es una lista de listas, en el que cada una de ellas es una fila del sudoku
    # El programa nos devolverá si existe una solución.
    # modificará las posiciones hasta dar con la solución (si esta existe)

    # Paso 1: escoger el primer hueco libre donde adivinar el numero
    fila, columna = encontrar_hueco(puzle)

    # Paso 1.1: si ya no queda ningun hueco, entonces lo tenemos hecho ya que solo permitimos entradas
    # validas
    if fila is None: # esto es verdad si la funcion encontar_hueco ha devulto None, None
        return True

    # Paso 2: si hay un hueco donde poner un número, entonces tenemos que hacer una elección
    # de un número entre el (1 - 9)
    for eleccion in range(1, 10):  # range(1,10) es 1, 2, 3, .... , 9
        # Paso 3 comprobar si el número elegido es valido.
        if es_valido(puzle, eleccion, fila, columna):
            # Paso 3.1: si el número elegido es válido vamos a colocarlo en su lugar en el puzle.
            puzle[fila][columna] = eleccion
            # Ahora volvemos a iterar usando este nuevo puzle.
            # Paso 4: de forma recurrente volvemos a llamar a nuestras funciones.
            if resolver_sudoku(puzle):
                return True
        # Paso 5: Si no es valido OR si nuestra eleccion no resuelve los criterios del puzle entonces
        # tenemos que volver a iterar y escoger un nuevo numero.
        puzle[fila][columna]=-1 # reseteamos el número elegido previamente

    # Paso 6: si ninguno de los numeros que hemos intentado funciona, entonces el sudoku no tiene 
    # solución.
    return False

if __name__=="__main__":
    ejemplo_sudoku = [
        [-1,-1,7,5,-1,-1,-1,-1,-1],
        [1,-1,-1,-1,6,-1,-1,9,-1],
        [9,-1,-1,-1,7,-1,-1,-1,1],

        [-1,-1,-1,-1,-1,4,6,-1,3],
        [-1,-1,-1,-1,-1,-1,-1,-1,5],
        [4,-1,8,-1,-1,-1,-1,7,-1],

        [-1,-1,-1,3,-1,7,-1,-1,-1],
        [-1,2,3,-1,1,-1,-1,6,-1],
        [-1,-1,1,-1,-1,-1,8,-1,-1]
    ]
    print(resolver_sudoku(ejemplo_sudoku))
    pprint(ejemplo_sudoku)
