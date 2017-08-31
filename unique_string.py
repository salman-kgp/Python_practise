#Code to check a string has unique charecters

#using hash_map

def is_unique(inp_str):
	c_dict = {}
	for c in inp_str:
		if c in inp_str:
			return False
		else:
			c_dict[c]=1
	return True


#no data structure , bruteforce

def is_unique_bf(inp_str):
	for i in range(len(inp_str)-1):
		for j in range(i+1,len(inp_str)):
			if inp_str[i] == inp_str[j]:
				return False
	return True

#no data structure , sorting

def is_unique_sort(inp_str):
	inp_str =sorted(inp_str)
	for i in range(1,len(inp_str)):
		if inp_str[i]==inp_str[i-1]:
			return False
	return True