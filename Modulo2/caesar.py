
# Cifrado Cesar

import string

ALFAFETO = string.ascii_lowercase

k = int(input('Introduzca k: '))

plaintext = input('Introduzca texto a cifrar: ')

ciphertext = ''
for l in plaintext:
    
    if l.lower() in ALFAFETO:
        p = ALFAFETO.find(l.lower())
        # algoritmo cesar
        c = (p + k) % 26
        
        if l.isupper():
            ciphertext += ciphertext.join(ALFAFETO[c].upper())
        else:
            ciphertext += ciphertext.join(ALFAFETO[c])
    else:
        ciphertext += ciphertext.join(l)
        
ciphertext