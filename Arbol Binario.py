


class Nodo:
    def __init__(self, palabra):
        self.palabra = palabra
        self.contador = 1
        self.izquierda = None
        self.derecha = None




def limpiar_texto(texto):
    signos = "¿?¡!.,;:\"'()[]{}«»…-_"
    for signo in signos:
        texto = texto.replace(signo, " ")
    texto = texto.lower()
    return texto.split()


def quitar_acentos(palabra):
    
    cambios = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ü": "u", "ñ": "n~"}
    resultado = ""
    for letra in palabra:
        if letra in cambios:
            resultado += cambios[letra]
        else:
            resultado += letra
    return resultado


def comparar(a, b):
    
    a_limpia = quitar_acentos(a)
    b_limpia = quitar_acentos(b)
    if a_limpia < b_limpia:
        return -1
    if a_limpia > b_limpia:
        return 1
    
    if a < b:
        return -1
    if a > b:
        return 1
    return 0


# ---------- Inserción ----------

def insertar(nodo, palabra):
    if nodo is None:
        return Nodo(palabra)

    resultado = comparar(palabra, nodo.palabra)
    if resultado < 0:
        nodo.izquierda = insertar(nodo.izquierda, palabra)
    elif resultado > 0:
        nodo.derecha = insertar(nodo.derecha, palabra)
    else:
        nodo.contador += 1  # palabra repetida
    return nodo


# ---------- Recorridos ----------

def inorden(nodo, lista):
    if nodo is not None:
        inorden(nodo.izquierda, lista)
        lista.append(nodo.palabra)
        inorden(nodo.derecha, lista)


def preorden(nodo, lista):
    if nodo is not None:
        lista.append(nodo.palabra)
        preorden(nodo.izquierda, lista)
        preorden(nodo.derecha, lista)


def postorden(nodo, lista):
    if nodo is not None:
        postorden(nodo.izquierda, lista)
        postorden(nodo.derecha, lista)
        lista.append(nodo.palabra)




def contar_nodos(nodo):
    if nodo is None:
        return 0
    return 1 + contar_nodos(nodo.izquierda) + contar_nodos(nodo.derecha)


def es_hoja(nodo):
    return nodo.izquierda is None and nodo.derecha is None


def contar_internos(nodo):
    if nodo is None or es_hoja(nodo):
        return 0
    return 1 + contar_internos(nodo.izquierda) + contar_internos(nodo.derecha)


def obtener_hojas(nodo, lista):
    if nodo is not None:
        if es_hoja(nodo):
            lista.append(nodo.palabra)
        obtener_hojas(nodo.izquierda, lista)
        obtener_hojas(nodo.derecha, lista)


def obtener_internos(nodo, lista):
    if nodo is not None:
        if not es_hoja(nodo):
            lista.append(nodo.palabra)
        obtener_internos(nodo.izquierda, lista)
        obtener_internos(nodo.derecha, lista)


def palabra_maxima(nodo):
    
    if nodo is None:
        return None
    while nodo.derecha is not None:
        nodo = nodo.derecha
    return nodo.palabra


def obtener_repetidas(nodo, lista):
    if nodo is not None:
        obtener_repetidas(nodo.izquierda, lista)
        if nodo.contador > 1:
            lista.append(f"{nodo.palabra} ({nodo.contador} veces)")
        obtener_repetidas(nodo.derecha, lista)


def dibujar_arbol(nodo, nivel=0, lado="Raíz"):
    
    if nodo is not None:
        print("    " * nivel + f"{lado}: {nodo.palabra}")
        dibujar_arbol(nodo.izquierda, nivel + 1, "I")
        dibujar_arbol(nodo.derecha, nivel + 1, "D")




def main():
    texto = input("Escribe una oración: ")
    palabras = limpiar_texto(texto)

    if len(palabras) == 0:
        print("No escribiste ninguna palabra.")
        return

    raiz = None
    for palabra in palabras:
        raiz = insertar(raiz, palabra)

    print("\nÁrbol:")
    dibujar_arbol(raiz)

    lista = []
    inorden(raiz, lista)
    print("\nInorden:  ", lista)

    lista = []
    preorden(raiz, lista)
    print("Preorden: ", lista)

    lista = []
    postorden(raiz, lista)
    print("Postorden:", lista)

    print("\nTotal de nodos:", contar_nodos(raiz))
    print("Nodos internos:", contar_internos(raiz))
    print("Palabra máxima:", palabra_maxima(raiz))

    hojas = []
    obtener_hojas(raiz, hojas)
    print("\nHojas:", hojas)

    internos = []
    obtener_internos(raiz, internos)
    print("Internos:", internos)

    repetidas = []
    obtener_repetidas(raiz, repetidas)
    print("\nPalabras repetidas:", repetidas)


main()