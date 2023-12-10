def main():
	lines = []
	with open("input.txt") as f:
		lines = f.read().split('\n')[:-1]

	# lines = ['RL', '', 'AAA = (BBB, CCC)', 'BBB = (DDD, EEE)', 'CCC = (ZZZ, GGG)', 'DDD = (DDD, DDD)', 'EEE = (EEE, EEE)', 'GGG = (GGG, GGG)', 'ZZZ = (ZZZ, ZZZ)']
	# lines = ['LLR', '', 'AAA = (BBB, BBB)', 'BBB = (AAA, ZZZ)', 'ZZZ = (ZZZ, ZZZ)']

	path = lines[0]

	data = {}
	for x in lines[2:]:
		node, direc = x.split('=')
		node = node.strip()
		r = []
		d = ''
		for y in direc:
			if y.isalpha():
				d += y
			elif len(d):
				r += [d]
				d = ''
		direc = r
		data[node] = direc

	count = 0
	pos = 'AAA'
	while pos != 'ZZZ':
		n = path[count%len(path)]

		if n == 'L':
			pos = data[pos][0]
		else:
			pos = data[pos][1]

		count += 1
	print(count)

if __name__ == '__main__':
	main()


