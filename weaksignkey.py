# Let's assume the secret key has 7 digits, each from the range of 0 to 9.

fp = open("wordlist.txt", "w")
for i in range (10):
	for j in range (10):
		for k in range (10):
			for l in range (10):
				for m in range (10):
					for n in range (10):
						for o in range (10):
							fp.write("%d%d%d%d%d%d%d\n" % (i,j,k,l,m,n,o));
fp.close()