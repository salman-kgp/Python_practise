'''
http://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0

Author: Salman Ahmad
'''

def sort_012s(arr):
	count_dict = {}
	for num in arr:
		count_dict[num] = count_dict.get(num,0)+1

	index = 0
	for i in range(count_dict.get(0,0)):
		arr[index] = 0
		index+=1
	for i in range(count_dict.get(1,0)):
		arr[index] = 1
		index+=1
	for i in range(count_dict.get(2,0)):
		arr[index] = 2
		index+=1
	
if __name__ == '__main__':
	test_cases = int(input())
	for i in range(test_cases):
		n = int(input())
		arr = [int(x) for x in input().strip().split(' ')]
		sort_012s(arr)
		for num in arr:
			print(num,end=" ")


