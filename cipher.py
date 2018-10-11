em = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,
'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,
't':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25,'0':26,'1':27,
'2':28,'3':29,'4':30,'5':31,'6':32,'7':33,'8':34,'9':35}

dm = { 0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j', 
10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q', 17:'r', 18:'s', 19:'t', 20:'u',
21:'v', 22:'w', 23:'x', 24:'y', 25:'z', 26:'0', 27:'1',
28:'2', 29:'3', 30:'4', 31:'5', 32:'6', 33:'7', 34:'8', 35:'9'}

def encipher(data, keytext, key):

	encrypted_data = ''
	temp = ''
	n = len(keytext)
	while (len(data) < len(keytext)):
		data += 'x'

	j = 0
	for i in range(0, len(data)):
		temp += dm[(em[data[i]] + em[keytext[j]]) % 36]
		j += 1
		j %= n

	for i in range(0, len(temp)):
		encrypted_data += dm[(em[temp[i]] + key) % 36]

	print("enciphered:", encrypted_data)
	return encrypted_data

def decipher(encrypted_data, keytext, key):

	decrypted_data = ''
	temp = ''
	n = len(keytext)

	for i in range(0, len(encrypted_data)):
		temp += dm[(em[encrypted_data[i]] - key + 36) % 36]

	j = 0
	for i in range(0, len(temp)):
		decrypted_data += dm[(em[temp[i]] - em[keytext[j]] + 36) % 36]
		j += 1
		j %= n

	print("deciphered:", decrypted_data)
	return decrypted_data
