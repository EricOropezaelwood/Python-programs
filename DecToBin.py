
def DecToBin(decimal_in):
    
	bin_rev = []
	bin_out = []
	n = decimal_in
	if (n==0):
		bin_out.append(0)
	else:
		while (n!=0):
			if(n%2==0):
				bin_rev.append(0)
				n=n/2
			else:
				bin_rev.append(1)
				n=(n-1)/2
		for x in range(0, len(bin_rev)):
			bin_out.append(bin_rev[len(bin_rev)-1-x])
	return(bin_out)

print(DecToBin(241))






