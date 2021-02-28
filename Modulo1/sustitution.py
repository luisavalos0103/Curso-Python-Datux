# Subtitución

def encripta(texto):
    
    import string
    ALFAFETO = string.ascii_lowercase
    
    llave = input("Ingrese la llave: ")
    ciphertext =""
    if len(llave)!=26:
        print("La llave debe tener 26 caracteres")
    elif not llave.isalpha():
        print("La llave tiene caracteres no alfabeticos")       
    else:
        for l in texto:
                    
            if l.lower() in ALFAFETO:
                c = ALFAFETO.find(l.lower())
        
                if l.isupper():
                    ciphertext += ciphertext.join(llave[c].upper())
                else:
                    ciphertext += ciphertext.join(llave[c].lower())
            else:
                ciphertext += ciphertext.join(l)
                
    print("Texto plano: ", texto)
    print("Texto encriptado: ", ciphertext)
    print("0")
            
encripta("hello, world")