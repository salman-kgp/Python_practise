#check if a string is permutation of other string

#with O(N) time complexity and O(N) space complexity
def is_permutation(w1,w2):
	if len(w1)!=len(w2):
		return False

	c_dict = {}
	for c in w1:
		c_dict[c] = c_dict.get(c,0)+1

	for c in w2:
		if c not in c_dict:
			return False
		else:
			c_dict[c]-=1
	for c in c_dict:
		if c_dict[c]!=0:
			return False
	return True


#by sorting O(NlogN) time complexity O(1) space complexity

def is_premutation_sort(w1,w2):
	if len(w1)!=len(w2):
		return False

	w1 = sorted(w1)
	w2 = sorted(w2)

	for i in range(len(w1)):
		if w1[i] != w2[i]:
			return False

	return True

