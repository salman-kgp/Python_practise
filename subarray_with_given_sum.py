'''
http://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0
Author: Salman Ahmad
'''

def subarray_with_sum(arr,target):
	start_index = 0
	last_index = 0
	curr_sum = arr[0]
	if curr_sum==target:
		print ("{} {}".format(start_index+1,last_index+1))
		return
	while last_index < len(arr)-1:
		last_index+=1
		curr_sum+=arr[last_index]
		while curr_sum>target and start_index<=last_index:
			curr_sum-=arr[start_index]
			start_index+=1

		if curr_sum==target:
			print ("{} {}".format(start_index+1,last_index+1))
			return
	print -1


if __name__ == '__main__':
	test_cases = int(input())
	for i in range(test_cases):
		n,target = [int(x) for x in input().split(' ')]
		arr = [int(x) for x in input().split(' ')]
		subarray_with_sum(arr,target)


