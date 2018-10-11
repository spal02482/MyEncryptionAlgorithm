def rlencode(data):
	old = data[0]
	count = 1
	encoded_data = ''
	for i in range(1, len(data)):
		if (data[i] != old):
			encoded_data += str(count)
			encoded_data += old
			count = 1
			old = data[i]
		else:
			count += 1
	encoded_data += (str(count) + old)
	print("encoded:", encoded_data)
	return encoded_data

def rldecode(data):
	number = 0
	decoded_data = ''
	for i in range(0, len(data)):
		if (str.isdigit(data[i]) == True):
			number = number * 10 + int(data[i])
		else:
			decoded_data += (data[i] * number)
			number = 0
	print("decoded:", decoded_data)
	return decoded_data

