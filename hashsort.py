import random
from time import perf_counter

def HashSort(array_to_sort):
	#O(2N)
	Start=min(array_to_sort)
	End=max(array_to_sort)

	allocate=[False]*(End-Start)

	#O(N)
	for i in range(len(array_to_sort)):
		try:
			allocate[array_to_sort[i]-Start]=True
		except:
			pass
	
	return Start, allocate

def HashedVals(hashsortarray, currentval):
	while hashsortarray[currentval+1]!=1:
		currentval+=1
	return currentval+1

sort1=[]
sort2=[]
count=0
length=10000000
for i in range(length):
	sort1.append(i)
	#sort1.append(2*i)
	sort2.append(i)
	#sort2.append(2*i)
	#sort2_tab.append(False)

random.shuffle(sort1)
random.shuffle(sort2)

t1_start=perf_counter()

sort1.sort()

t1_stop=perf_counter()
#print('elapsed time: ',t1_stop, t1_start)
print('built-in sort: ',t1_stop-t1_start)

t2_start=perf_counter()

start, hashedsort=HashSort(sort2)

t2_stop=perf_counter()

print('hashed sort: ',t2_stop-t2_start)

currentval = HashedVals(hashedsort, start)
print('second val: ', currentval)

for i in range(10):
	currentval=HashedVals(hashedsort, currentval)
	print(currentval)
