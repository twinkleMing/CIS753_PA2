from bitstring import BitArray
from Crypto.PublicKey import RSA
from Crypto.Random import random
from Crypto.Util import number
from Crypto import Random
import math
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]


class key:
	def __init__(self, p, q, n, e, d):
		self.p = p; self.q = q; self.n = n; self.e = e; self.d = d

def Exponent(x,e,n):
	e_bit = BitArray(bin(e))
	l = len(e_bit)
	y = 1
	for i in range(l): 
		if e_bit[l-1-i] ==True: y = (y*x) %n
		x = (x*x) % n 
	return y % n

def Ex_Eulidean(a,b):
	r0 = a; r1 = b
	x0 = 1; y0 = 0
	x1 = 0; y1 = 1
	while r1 != 0:
		q = r0 // r1
		r2 = r0 - q*r1
		x2 = x0 - q*x1
		y2 = y0 - q*y1
		r0 = r1; r1 = r2
		x0 = x1; x1 = x2
		y0 = y1; y1 = y2
	return [r0, x0, y0]


def Primality_Test(n):
	for i in range(len(prime)):
		if n%prime[i] == 0: return False
	n_p = n-1
	k = 0
	(quotient, remainder) = divmod(n_p,2)
	while remainder == 0:
		n_p = quotient
		k = k+1
		(quotient, remainder) = divmod(n_p,2)
	m = n_p
	for j in range(5):
		flag = False
		a = random.randint(1, n-1)
		b = Exponent(a,m,n)
		if b == 1: 
			flag = True
			continue
		for i in range(k):
			if (b+1)%n == 0:
				flag = True
				break
			b = (b * b) % n
		if flag == False: return False
	return True


def RSA_keygen(num):
	rng = Random.new().read
	p = number.getRandomNBitInteger(num/2, rng)
	while Primality_Test(p) == False:
		p = number.getRandomNBitInteger(num/2, rng)
	q = number.getRandomNBitInteger(num/2, rng)
	while Primality_Test(q) == False or q == p:
		q = number.getRandomNBitInteger(num/2, rng)
	n = p * q
	phi_n = (p-1) * (q-1)
	k = 0
	while True:
		while  True: 
			e = random.randint(1, phi_n)
			##k = k + 1
			##print k
			r = Ex_Eulidean(e, phi_n)
			if r[0] == 1: break
		d = r[1] % phi_n
		d_bit = BitArray(bin(d))
		l = len(d_bit)
		#print "l is: " + str(l)
		if l > num - 4: break


	nn = BitArray(uint = n, length = num).hex
	ee = BitArray(uint = e, length = num).hex
	dd = BitArray(uint = d, length = num).hex
        pp = BitArray(bin(p)).hex
	qq = BitArray(bin(q)).hex
	return [pp, qq, nn, ee, dd]



def cryption(n,e,text):
	text_int = BitArray(hex = text).uint
	e_int = BitArray(hex = e).uint
	n_int = BitArray(hex =n).uint
	cipher = Exponent(text_int, e_int, n_int)
	l = int(math.ceil((len(bin(cipher))-2) / 4.0) * 4)
	return BitArray(uint = cipher, length = l).hex









