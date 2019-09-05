from hashlib import sha256 as sha
import sys,getopt,time

def pow(msg, diff):
	# second try using simple math
	# gets target difficulty (the int is represented by its binary and the compiler interprets it as binary
	target = 2 ** (256-int(diff))
	for nonce in range(2**30) : #maximum tries(nonce) = 2^30  
		# gets the hash of the hash of the string passed and the nonce
		# casts to string to be able to work with the A0..... id
		haash = sha(sha(str(msg).encode('utf-8')+str(nonce).encode('utf-8')).digest()).hexdigest()
		# Checks if num is smaller than target (ej. target: 00100000   num: 000011111) This gives the leading zeroes
		# python implementation of comparing int is much faster (implemented in C) and uses binary directly 
		if int(haash, 16) < target:
			return(haash, nonce)
	print("POW failed after %d tries" % nonce)
	# --------- FIRST TRY USING STRINGS (Slow AF)
	#
	# dif = int(int(diff)/4)
	# zeros = '0'*dif
	# for nonce in range(2**30):

	#--------- use this haash in case of msg being a hexadecimal -------------
	
	# 	haash = sha(sha(bytes.fromhex(msg)+bytes(nonce)).digest()).digest()
	# ------------------------------------------------------------
	# 	if haash.hex()[:dif] == zeros:
	# 		return(haash.hex(), nonce)
	# 	print(nonce)
	# print(msg,diff)

def main(argv):
	if len(argv) < 4:
		print('pow.py -d <difficulty in bits> -i <input>')
		sys.exit(2)
	try:
		opts, args = getopt.getopt(argv,"d:i:")
	except getopt.GetoptError:
		print('pow.py -d <difficulty in bits> -i <input>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('pow.py --difficulty <difficulty in bits> --id <input>')
			sys.exit()
		elif opt == "-d":
			diff  = arg
		elif opt == "-i":
			string = arg
	start = time.time()
	res,nnc = pow(string, diff)
	runtime = time.time() - start
	print('[+] Solved in %.4f  sec ( %.2f Mhash/sec)'% (runtime,(nnc/runtime)/1000))
	print('[+] Solution: ' + res)
	print('[+] Input: ' + string)
	print('[+] Nonce: ' + str(nnc))

if __name__ == '__main__':
	main(sys.argv[1:])


