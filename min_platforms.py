"""
http://practice.geeksforgeeks.org/problems/minimum-platforms/0

Author : Salman Ahmad
"""

def min_platforms(arrival,exits):
	time_adds = {}

	for i in range(len(arrival)):
		if exits[i] <= arrival[i]:
			exits[i]+=2400

	for t in arrival:
		time_adds[t] = time_adds.get(t,0)+1

	for t in exits:
		time_adds[t] = time_adds.get(t,0)-1

	full_list = arrival+exits

	sorted_list = sorted(full_list)

	min_pltforms = 0
	count = 0

	for t in sorted_list:
		count+=time_adds[t]
		if count>min_pltforms:
			min_pltforms = count

	return min_pltforms



if __name__ == '__main__':
	test_cases = int(input())
	for i in range(test_cases):
		n=input()
		arrivals = [int(x) for x in input().strip().split(' ') if x!='']
		exits = [int(x) for x in input().strip().split(' ') if x!='']
		print (min_platforms(arrivals,exits))
