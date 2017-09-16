'''
http://practice.geeksforgeeks.org/problems/missing-number-in-array/0

Author:Salman Ahmad
'''


def find_missing_number(arr,n):
	sum_to_n = (n*(n+1))/2
	arr_sum = sum(arr)
	return sum_to_n - arr_sum

if __name__=='__main__':
	test_cases = int(input())
	for i in range(test_cases):
		n = int(input())
		arr = [int(x) for x in input().split(' ')]
		print find_missing_number(arr,n)
