
import string

def cesar_cipher(text, key, cipher=True):

	key = key if cipher else -key # ternary
	
	crypted_text = ""
	for char in text:
		crypted_char = chr((ord(char) + key) % 1_114_112)
		crypted_text += crypted_char

	return crypted_text



def brute_force_cesar_cipher(crypted_text):
	for potential_key in range(1, 1_114_112):
		potential_initial_text = cesar_cipher(crypted_text, potential_key, cipher=False)

		for char in potential_initial_text:
			if char in string.printable:
				print(potential_key)
				print(potential_initial_text)
				print("-----")
				break



def vigenere_cipher(text, password, cipher=True):
	list_of_keys = [ord(char) for char in password]
	crypted_text = ""

	for index, char in enumerate(text):
		current_key = list_of_keys[index % len(list_of_keys)]
		crypted_char = cesar_cipher(text=char, key=current_key, cipher=cipher)
		crypted_text += crypted_char

	return crypted_text





# crypted_text = cesar_cipher(text="lapin", key=554)
# print(crypted_text)

# initial_text = cesar_cipher(text=crypted_text, key=3_000_000, cipher=False)
# print(initial_text)


# brute_force_cesar_cipher(crypted_text)


crypted_text = vigenere_cipher(text="Bonjour tout le monde !", password="Azerty12345")
print(crypted_text)

initial_text = vigenere_cipher(text=crypted_text, password="Azerty12345", cipher=False)
print(initial_text)
