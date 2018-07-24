'''
Eric Oropezaelwood
17 September 2015
Assignment 4
Read in a file containing DNA information. Create a dictionary from the file and then check individual RSID's to see if they have a risk for diabetes and their skin type.
'''
import sys

d = {}

def parseFile(fname):
	fo = open(fname, "r")
	for line in fo:
		# creates dictionary while skipping any lines beginning
		# with "#"
		if line[0] != "#":			
			par = line.split()
			rsid = par[0]
			geno = par[3]
			d[rsid] = geno
	return d
	fo.close()

def checkSkinType(geno):
	if geno == "AA":
		print("Probably light-skinned, European ancestry")
	elif geno == "AG":
		print("Probably mixed African/European ancestry")
	elif geno == "GG":
		print("Probably darker-skinned, Asian or African ancestry")
	else:
		print("No DNA info on Skin Type")

def checkType2Diabetes(geno):
	if geno == "CG":
		print("1.3x Increased risk for Type-2 Diabetes")
	elif geno == "CC":
		print("1.3x Increased risk for Type-2 Diabetes")
	elif geno == "GG":
		print("Normal risk for Type-2 Dibetes")
	else:
		print("No DNA info on Ty[e-2 Diabetes")

def main():
	fname = sys.argv[1]
	print("Parsing ", fname)
	#set dictionary equal to result of the function parseFile
	d = parseFile(fname)

	checkType2Diabetes(d["rs7754840"])
	checkSkinType(d["rs1426654"])
	
main()







