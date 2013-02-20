from funcs import *
import sys
import fileinput


while True:
	print "please input the function you want to perform:"
	print "K: RSA key pair generation	E: encryption	D: decryption	Q: quit"
	command = sys.stdin.readline()
	if command == "K\n":
		while True:
    			try:	
				print "please print a valid number of bits in keys:"
			 	num = int(sys.stdin.readline())
	        		break
			except ValueError:
        			print "Invalid number.  Try again..."
		key = RSA_keygen(num)
		keygen = open('keygen.txt', 'w')
		secret = open('secret.txt', 'w')		
		keygen.write(key[2] + '\n\n' + key[3] + '\n\n' + key[4])
		secret.write(key[0] + '\n\n' + key[1])		
		keygen.close()
		secret.close()
		##encrypt = open('encrypt.txt', 'w')
		##rng = Random.new().read
		##text = BitArray(uint = number.getRandomNBitInteger(512, rng), length = 512).hex
		##print text
		##encrypt.write(key[2] + '\n\n' + key[3] + '\n\n' + text)
		##encrypt.close()
		continue
	if command == "E\n":
		f = open('encrypt.txt', 'r')
		n = f.readline()
		f.readline()
		e = f.readline()
		f.readline()
		text = f.readline()
		f.close()
		cipher =  cryption(n,e,text)
		print cipher
		##decrypt = open('decrypt.txt', 'w')
		##decrypt.write(key[2] + '\n\n' + key[4] + '\n\n' + cipher)
		##decrypt.close()
		continue
	if command == "D\n":
		f = open('decrypt.txt', 'r')
		n = f.readline()
		f.readline()
		d = f.readline()
		f.readline()
		cipher = f.readline()
		f.close()
		text_re =  cryption(n,d,cipher)
		print text_re
		continue
	if command == "Q\n":
		break
	else: 
		print "The command you input is incorrect!"
		print "K: RSA key pair generation	E: encryption	D: decryption	Q: quit"


