#modificado para que pida la clave nuevamente al descifrar el msj y deba resolver una ecuación si olvida la clave
import random


def cifrar(texto, clave):
    texto_cifrado = ""
    for letra in texto:
        if letra.isalpha():
            if letra.isupper():
                texto_cifrado += chr((ord(letra) + clave - 65) % 26 + 65)
            else:
                texto_cifrado += chr((ord(letra) + clave - 97) % 26 + 97)
        else:
            texto_cifrado += letra
    return texto_cifrado


def descifrar(texto, clave):
    texto_descifrado = ""
    for letra in texto:
        if letra.isalpha():
            if letra.isupper():
                texto_descifrado += chr((ord(letra) - clave - 65) % 26 + 65)
            else:
                texto_descifrado += chr((ord(letra) - clave - 97) % 26 + 97)
        else:
            texto_descifrado += letra
    return texto_descifrado


def operacion_matematica():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    respuesta_correcta = a + b
    print(f"Para recuperar la clave, resuelva la siguiente operación: {a} + {b}")
    respuesta_usuario = int(input("Ingrese su respuesta: "))
    return respuesta_usuario == respuesta_correcta


def main():
    texto = input("Ingrese el texto a cifrar: ")
    clave = int(input("Ingrese la clave para cifrar: "))
    texto_cifrado = cifrar(texto, clave)
    print("Texto cifrado: ", texto_cifrado)

    intentos = 0
    while intentos < 3:
        clave_para_descifrar = int(input("Ingrese la clave para descifrar: "))
        texto_descifrado = descifrar(texto_cifrado, clave_para_descifrar)
        if texto_descifrado == texto:
            print("Texto descifrado correctamente: ", texto_descifrado)
            return
        else:
            print("Clave incorrecta. Intente nuevamente.")
            intentos += 1

    print("Ha excedido el número de intentos permitidos.")
    if operacion_matematica():
        print(f"La clave correcta era: {clave}")
        print("Texto descifrado: ", texto)
    else:
        print("Respuesta incorrecta. No se puede recuperar la clave.")


if __name__ == "__main__":
    main()
