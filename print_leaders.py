'''
http://practice.geeksforgeeks.org/problems/leaders-in-an-array/0

Author: Salman Ahmad
'''

def get_leaders(arr):
	is_leader = [False]*len(arr)
	index = len(arr)-1
	max_val = -1
	while index>=0:
		if arr[index]>max_val:
			is_leader[index]=True
			max_val = arr[index]
		index-=1
	for i in range(len(arr)):
		if is_leader[i]:
			print (arr[i],end=" ")

	print ()




if __name__ == '__main__':
	test_cases = int(input())
	for i in range(test_cases):
		n=input()
		arr = [int(x) for x in input().strip().split(' ')]
		get_leaders(arr)

