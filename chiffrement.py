def chiffre_cesar(string, nb_decal):
    if not string.isalpha():
        print("La chaîne doit contenir uniquement des lettres.")
    string_aux = "" 
    for c in string:
        if (c.isupper()):
            string_aux += chr((ord(c) + nb_decal-65) % 26 + 65) # Code ascci [A-Z] = [65-90] : -65 piur ramener à 0-25.
        else:
            string_aux += chr((ord(c) + nb_decal - 97) % 26 + 97) # Code ascci [a-z] = [97-122] : -97 piur ramener à 0-25


    return string_aux


def dechiffre_cesar(string,nb_decal):
    return chiffre_cesar(string, -nb_decal)

print(chiffre_cesar("Bonjour", 1))
print(dechiffre_cesar("Cpokpvs", 1))

def brute_force_cesar(string):
    for i in range(1, 26):  
        print(f"Décalage de {i} caracteères ===> {dechiffre_cesar(string, i)}")

brute_force_cesar("Cpokpvs")



def chiffre_vigenere(string, key):
    string_aux = ""
    key = key.lower() 
    k = 0  
    for c in string:
        decal = ord(key[k % len(key)]) - ord('a') 
        string_aux += chiffre_cesar(c, decal)
        k += 1
            

    return string_aux

def dechiffre_vigenere(string, key):
    string_aux = ""
    key = key.lower() 
    k = 0  
    for c in string:
        decal = ord(key[k % len(key)]) - ord('a')
        string_aux += dechiffre_cesar(c, decal)
        k += 1
            
    return string_aux

print(chiffre_vigenere("Bonjour", "cle"))
print(dechiffre_vigenere("Dzrlzyt", "cle"))