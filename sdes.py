# define the S-box tables globally, so that
# the S-box tables are not constructed every time fk() is called
S0 = [[[0, 1], [0,0], [1,1], [1,0]],
	[[1,1], [1,0], [0,1], [0,0]],
	[[0,0], [1,0], [0,1], [1,1]],
	[[1,1], [0,1], [1,1], [1,0]]]
S1 = [[[0,0], [0,1], [1,0], [1,1]],
	[[1,1], [0,0], [0,1], [1,1]],
	[[1,1], [0,0], [0,1], [0,0]],
	[[1,0], [0,1], [0,0], [1,1]]]

# given a 10-bit key, generate two 8-bit subkeys
def keygen(key):
	# permute a 10-bit key
	def P10(key): return [key[2], key[4], key[1], key[6], key[3], key[9], key[0], key[8], key[7], key[5]]

	# given a 10-bit key, return an 8-bit permutation of it
	def P8(key): return [key[5], key[2], key[6], key[3], key[7], key[4], key[9], key[8]]

	# given a 10-bit block,
	# perform a circular left shift separately on the 1st and 2nd five bits
	def shift(key): 
		return key[1:5] + [key[0]] + key[6:10] + [key[5]]
		# return [key[1], key[2], key[3], key[4], key[0], key[6], key[7], key[8], key[9], key[5]]

	# generate the keys
	k = shift(P10(key))
	return P8(k), P8(shift(shift(k)))

# initial permutation of 8-bit block
def ip(p): return [p[1], p[5], p[2], p[0], p[3], p[7], p[4], p[6]]

# final permutation of 8-bit block
def ip_inverse(p): return [p[3], p[0], p[2], p[4], p[6], p[1], p[7], p[5]]

# given an 8-bit number n and an 8-bit subkey k, mung them
def fk(n, k):
	# Given two bits, bit1 and bit2, return bit1 XOR bit2
	def xor(bit1, bit2): return 0 if bit1 == bit2 else 1

	# given a 4-bit number n and an 8-bit subkey k, mung them
	def F(n, k):
		# expand/permute
		ep = [xor(n[3], k[0]), xor(n[0], k[1]), xor(n[1], k[2]), xor(n[2], k[3]), 
			xor(n[1], k[4]), xor(n[2], k[5]), xor(n[3], k[6]), xor(n[0], k[7])]

		# get two bits from S-box S0
		row0 = ep[0] * 2 + ep[3] 
		column0 = ep[1] * 2 + ep[2]
		a = S0[row0][column0]

		# get two bits from S-box S1
		row1 = ep[4] * 2 + ep[7]
		column1 = ep[5] * 2 + ep[6]
		b = S1[row1][column1]

		# combine the two bits, and permute again
		p = a + b
		return [p[1], p[3], p[2], p[0]]

	l = n[:4]
	r = n[4:]
	m = F(r, k)
	return [xor(l[i], m[i]) for i in range(4)] + r

# given an 8-bit input, interchange the left and right 4 bits
def switch(input): 
	return input[4:] + input[:4]
	# return [input[4], input[5], input[6], input[7], input[0], input[1], input[2], input[3]]

# given an 8-bit block plaintext and a 10-bit key, 
# return an 8-bit block of ciphertext
def encrypt(plaintext, key):
	key1, key2 = keygen(key)
	return ip_inverse(fk(switch(fk(ip(plaintext), key1)), key2))

# given an 8-bit block of ciphertext and the 10-bit key used to generate it,
# return the original 8-bit block of plaintext
def decrypt(ciphertext, key):
	key1, key2 = keygen(key)
	return ip_inverse(fk(switch(fk(ip(ciphertext), key2)), key1))
