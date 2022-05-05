abc = {
        'A': 'E', 'B': 'F', 'C': 'G', 'D': 'H', 'E': 'I',
        'F': 'J', 'G': 'K', 'H': 'L', 'I': 'M', 'J': 'N',
        'K': 'O', 'L': 'P', 'M': 'Q', 'N': 'R', 'O': 'S',
        'P': 'T', 'Q': 'U', 'R': 'V', 'S': 'W', 'T': 'X',
        'U': 'Y', 'V': 'Z', 'W': 'A', 'X': 'B', 'Y': 'C',
        'Z': 'D', 
        'a': 'e', 'b': 'f', 'c': 'g', 'd': 'h', 'e': 'i',
        'f': 'j', 'g': 'k', 'h': 'l', 'i': 'm', 'j': 'n',
        'k': 'o', 'l': 'p', 'm': 'q', 'n': 'r', 'o': 's',
        'p': 't', 'q': 'u', 'r': 'v', 's': 'w', 't': 'x',
        'u': 'y', 'v': 'z', 'w': 'a', 'x': 'b', 'y': 'c',
        'z': 'd'
    }


def Encriptar(Frase):
    FraseEnc = '' #str vacio
    for letra in Frase: #recorro Frase letra por letra
        encontrado = False
        for x,y in abc.items():
            if letra == x:
                FraseEnc += y #fraseEnc.append(y)
                encontrado = True
        if not encontrado: #if encontrado == False
                            # if encontrado != True
            FraseEnc += letra
    print("Cadena encriptada: ", FraseEnc)

def Desencriptar(Frase):
    FraseDes = ''
    for letra in Frase:
        encontrado = False
        for x,y in abc.items():
            if letra == y:
                FraseDes += x #fraseEnc.append(x)
                encontrado = True
        if not encontrado: #if encontrado == False
            FraseDes += letra
    print("Cadena desencriptada: ", FraseDes)
