# Problem Set 5 Spring 2018
# Eric Oropezaelwood
#
# Using census data of last names produce a histogram of hashed values?
import sys
import random
import math
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


l=200
filename = sys.argv[1]


randomlySelectedNames=[]
newArr=[]
newArr2=[]
collisions=[]

# get 50% random names from input file
with open(filename) as f:
	for line in f:
		newArr.append(line)

for i in newArr:
	i = i.split(" ",1)
	newArr2.append(i[0])

namesSize=len(newArr2)
halfSize=namesSize//2


for i in range(0,halfSize):
	index=random.choice(newArr2)
	randomlySelectedNames.append(index)
	newArr2.remove(index)

#print(randomlySelectedNames)

# make array to count collisions
for i in range(0,200):
	collisions.append(0)

# fake the hash
hashFake=[]
for name in randomlySelectedNames:
	f=0
	for i in range(0,len(name)):
		f=f + (ord(name[i])-ord('A')+1)
		f=f%l;
	hashFake.append(f)
	# increment colisions
	collisions[f] += 1

#find largest hashed amount
largest = 0
for i in range(0,len(collisions)):
	if (collisions[i] > largest):
		largest = collisions[i]

print(collisions)

num_bins = 200
n, bins, patches = plt.hist(hashFake, num_bins, facecolor='blue', alpha=0.5)
plt.xlabel('hash location')
plt.ylabel('# of times hashed at this location')
plt.show()



# Applies to 2(c)

name_index = []
name_index.extend(range(0,len(randomlySelectedNames)))
hash_uniform = []
rb_tree = []
theta = []

for i in name_index:
	if((i/halfSize) < 1):
		hash_uniform.append(0)
	else:
		hash_uniform.append(i/halfSize)
	rb_tree.append(2*np.log(i+1))
	theta.append(i/75)


plt.plot(name_index,hashFake)
plt.plot(name_index,hash_uniform,linewidth=4)
plt.plot(name_index,rb_tree,linewidth=4)
plt.plot(name_index,theta,linewidth=4)
plt.title('Hash entries and longest chain')
plt.ylabel('Longest Chain')
plt.xlabel('Hash Table')
plt.show()