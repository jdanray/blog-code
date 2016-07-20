alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
m = len(alphabet)
a = 5
b = 8
inverse_a = inverse_mod(a, m)

def encrypt(plaintext):
	ciphertext = ''
	for p in plaintext:
		x = alphabet.find(p.upper())
		if x != -1:
			c = (a * x + b) % m
			ciphertext += alphabet[c]
	return ciphertext
			
def decrypt(ciphertext):
	plaintext = ''
	for c in ciphertext:
		p = (inverse_a * (alphabet.find(c) - b)) % m 
		plaintext += alphabet[p]
	return plaintext
