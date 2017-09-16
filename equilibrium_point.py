'''
http://practice.geeksforgeeks.org/problems/equilibrium-point/0

Author :Salman Ahmad
'''

def find_equilibrium(arr):
	if len(arr)==1:
		return 1
	if len(arr)==2:
		return -1

	for i in range(1,len(arr)):
		arr[i]+=arr[i-1]

	for i in range(1,len(arr)-1):
		if arr[i-1]==(arr[-1]-arr[i]):
			return i+1

	return -1



if __name__ == '__main__':
	test_cases = int(input())
	for i in range(test_cases):
		n=input()
		arr = [int(x) for x in input().strip().split(' ')]
		print(find_equilibrium(arr))