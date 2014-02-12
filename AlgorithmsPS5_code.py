

def add(tpl,pq):

	if len(pq) == 0:
	#this is the base case when length = 0 
		pq.insert(0,tpl)

	if tpl in pq:
		return pq
	for i in range (0 ,len(pq)):
	#goes through the range of pq
		if ((pq[i][1]) >= tpl[1]):
		#if the posiiton is less than or equal insert 
			pq.insert(i,tpl)
			break
		if (i == len(pq)-1):
		#this is the tie case 
			pq.insert(i+1,tpl)
	return pq

def create_pq(string):
	x = []
	y = []
	#initialize two arrays 
	alphabet = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for i in range (0,len(alphabet)):
		#iterate through and add the priority/char to each array 
		x.insert(i,alphabet[i])
		y.insert(i,string.count(alphabet[i]))
	current_list = zip(x,y)
	#zip them together into an array of tuples 
	pq = []
	#Initialize a pq variable 
	for i in range (0, len(current_list)):
		pq = add(current_list[i], pq)
		#add in our zipped list, in order 
	return pq

def huff(pq,tree):
	#print len(pq)
	if (len(pq) == 1):
		return tree
	else:
		i = pq.pop(0)
		#print "We popped:" + i[0] 
		j = pq.pop(0)
		new_i = i[0] + j[0]
		#print new_i
		new_j = i[1] + j[1]
		new_t = (new_i,new_j)
		tree = add(i,tree)
		pq = add(new_t,pq)
		tree = add(j,tree)
		return huff(pq,tree)
 

test_pq =[]
test_pq = create_pq("abc")
final = []
print huff(test_pq,final)
