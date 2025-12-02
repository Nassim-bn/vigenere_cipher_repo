def chiffre_cesar(string, nb_decal):
    if not string.isalpha():
        print("La chaîne doit contenir uniquement des lettres.")
    string_aux = ""
    decal_aux = nb_decal % 26  # Optimisé : calculé une seule fois
    # In ascii, [a-z] = [97-122] et [A-Z] = [65-90]
    for c in string:
        ascii_code = ord(c) + decal_aux
        if c.islower():
            if ascii_code > ord('z'):
                ascii_code -= 26
        elif c.isupper():
            if ascii_code > ord('Z'):
                ascii_code -= 26

        string_aux += chr(ascii_code)

    return string_aux


def dechiffre_cesar(string,nb_decal):
    return chiffre_cesar(string, -nb_decal)

print(chiffre_cesar("Bonjour", 1))
print(dechiffre_cesar("Cpokpvs", 1))

def brute_force_cesar(string):
    for i in range(1, 26):  
        print(f"Décalage de {i}: {dechiffre_cesar(string, i)}")

brute_force_cesar("Cpokpvs")



def chiffre_vigenere(string, key):
    string_aux = ""
    key = key.lower() 
    k = 0  
    for c in string:
        decal = ord(key[k % len(key)]) - ord('a')  # décalage de la clé
        string_aux += chiffre_cesar(c, decal)      # applique César
        k += 1
            

    return string_aux

def dechiffre_vigenere(string, key):
    string_aux = ""
    key = key.lower() 
    k = 0  
    for c in string:
        decal = ord(key[k % len(key)]) - ord('a')  # décalage de la clé
        string_aux += dechiffre_cesar(c, decal)    # applique César inversé
        k += 1
            
    return string_aux

print(chiffre_vigenere("Bonjour", "cle"))
print(dechiffre_vigenere("Dqopxvs", "cle"))