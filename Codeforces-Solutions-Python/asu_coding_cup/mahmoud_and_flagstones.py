if __name__ == '__main__':
	n = int(input())
	input_v = input().split()
	flagstones = {}
	subsets = 0
	
	for item in input_v:
		item = int(item)
		if item in flagstones:
			flagstones[item] += 1
		else:
			flagstones[item] = 1
			
	for item in flagstones:
		subset = 2 ** flagstones[item] - 1
		subsets += subset
	print(subsets % (10 ** 9 + 7))
