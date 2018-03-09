import string
plaintext = input('Enter the message you want to encrypt: ')
plaintext = plaintext.replace(' ', '')
plaintext = plaintext.upper()
plaintext = list(plaintext)

sharedPrime = int(input('Enter a large prime number to share: '))
if sharedPrime > 1:
	for i in range(2, sharedPrime):
		if (sharedPrime % i) == 0:
			print(sharedPrime, 'is not a prime number')
			break
			
	print('Publicly shared prime is ', sharedPrime)
else:
	print(sharedPrime, 'is not a prime number')
	exit()

sharedGenerator = int(input('Enter a shared generator less than ' + str(sharedPrime) + ': ' ))
if sharedGenerator < sharedPrime:
	print('Publicly shared generator is ', sharedGenerator)
else:
	print(sharedGenerator, 'is larger than' + sharedPrime)
	exit()

secretA = int(input('Enter a secret key for person A: '))
secretB = int(input('Enter a secret key for person B: '))

# Person A sends person B = g^a mod p
A = (sharedGenerator**secretA) % sharedPrime
print('Person A sends over public channel: ', A)
 
# Person B sends person A = g^b mod p
B = (sharedGenerator ** secretB) % sharedPrime
print('Person B sends over public channel: ', B)

print('Privately calculated key: ')
# Person A computes: s = B^a mod p
sharedSecretA = (B ** secretA) % sharedPrime
print('Person A\'s Shared Secret: ', sharedSecretA)
 
# Person B computes: s = A^b mod p
sharedSecretB = (A ** secretB) % sharedPrime
print('Person B\'s Shared Secret: ', sharedSecretB)

print('\n``````````The Key has been chosen```````````\n')

letters = list(string.ascii_uppercase)
numbers = list()
for i in range(0,26):
	numbers.append(i)

dictionary = dict(zip(letters, numbers))

plainDictionary = {}

for key, val in dictionary.items():
	for i in plaintext:
		if i == key:
			plainDictionary[i] = val

ciphertextVals = list()

for i in plaintext:
	for key, val in dictionary.items():
		if i == key:
			y = (val + sharedSecretA) % 26
			ciphertextVals.append(y)

ciphertext = ''

for i in ciphertextVals:
	for key, val in dictionary.items():
		if i == val:
			ciphertext = ciphertext + key

print('Ciphertext: ', ciphertext)