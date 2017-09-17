'''
https://www.udemy.com/data-science-natural-language-processing-in-python

Author : Salman Ahmad

time complexity:O(n)
space complexity :O(1)
'''


def remove_duplicates(arr):
	curr_index = 1
	moving_index = 1

	while moving_index<len(arr):
		while moving_index<len(arr) and arr[moving_index]== arr[curr_index-1] :
			moving_index+=1
		if moving_index>=len(arr):
			break
		arr[curr_index]=arr[moving_index]
		curr_index+=1
		moving_index+=1
	print arr[:curr_index]