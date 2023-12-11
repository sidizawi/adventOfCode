def main():
	lines = []
	with open("input.txt") as f:
		lines = f.read().split('\n')[:-1]

	# lines = ['0 3 6 9 12 15', '1 3 6 10 15 21', '10 13 16 21 30 45']

	sm = 0
	
	for line in lines:
		r = [[int(x) for x in line.split()]]

		while not all([x == 0 for x in r[-1]]):
			x = r[-1]
			r += [[]]
			for i in range(1, len(x)):
				r[-1] += [x[i] - x[i - 1]]


		res = 0
		for x in r[::-1][1:]:
			res = x[0] - res

		# print(res)
		# if (res <= 0):
		# 	print(r)

		sm += res

	print(sm)

if __name__ == '__main__':
	main()


