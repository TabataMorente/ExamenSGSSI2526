#!/usr/bin/env python3
from collections import Counter
import sys

if len(sys.argv) < 2:
    print("Uso: python3 descifrado.py archivo.txt")
    sys.exit(1)

archivo = sys.argv[1]

try:
    with open(archivo, "r", encoding="utf-8") as f:
        texto = f.read()
except FileNotFoundError:
    print(f"Error: archivo '{archivo}' no encontrado.")
    sys.exit(1)

print("=== TEXTO CIFRADO ORIGINAL ===")
print(texto)
print("\n" + "="*40 + "\n")

abecedario = {
    'A': '',
    'B': '',
    'C': '',
    'D': '',
    'E': '',
    'F': '',
    'G': '',
    'H': '',
    'I': '',
    'J': '',
    'K': '',
    'L': '',
    'M': '',
    'N': '',
    'Ñ': '',
    'O': '',
    'P': '',
    'Q': '',
    'R': '',
    'S': '',
    'T': '',
    'U': '',
    'V': '',
    'W': '',
    'X': '',
    'Y': '',
    'Z': ''
}

letras = [c.upper() for c in texto if c.isalpha()]
conteo = Counter(letras)
orden_cifrado = [letra for letra, _ in conteo.most_common()]
frecuencia_espanol = list("EAOLSNDRUITCPMYQBHGFVJÑZXKW")

i = 0
for letra in orden_cifrado:
    if letra not in abecedario or abecedario[letra] == '':
        while i < len(frecuencia_espanol) and frecuencia_espanol[i] in abecedario.values():
            i += 1
        if i < len(frecuencia_espanol):
            abecedario[letra] = frecuencia_espanol[i]
            i += 1

def descifrar(texto, subs):
    resultado = ""
    for c in texto:
        if c.isalpha():
            letra_mayus = c.upper()
            if letra_mayus in subs:
                sustituta = subs[letra_mayus]
                resultado += sustituta.lower() if c.islower() else sustituta
            else:
                resultado += c
        else:
            resultado += c
    return resultado

mensaje_descifrado = descifrar(texto, abecedario)
print("=== TEXTO DESCIFRADO ===")
print(mensaje_descifrado)

