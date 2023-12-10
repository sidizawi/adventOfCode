import math

def main():
	lines = []
	with open("input.txt") as f:
		lines = f.read().split('\n')[:-1]

	# lines = ['RL', '', 'AAA = (BBB, CCC)', 'BBB = (DDD, EEE)', 'CCC = (ZZZ, GGG)', 'DDD = (DDD, DDD)', 'EEE = (EEE, EEE)', 'GGG = (GGG, GGG)', 'ZZZ = (ZZZ, ZZZ)']
	# lines = ['LLR', '', 'AAA = (BBB, BBB)', 'BBB = (AAA, ZZZ)', 'ZZZ = (ZZZ, ZZZ)']
	# lines = ['LR', '', '11A = (11B, XXX)', '11B = (XXX, 11Z)', '11Z = (11B, XXX)', '22A = (22B, XXX)', '22B = (22C, 22C)', '22C = (22Z, 22Z)', '22Z = (22B, 22B)', 'XXX = (XXX, XXX)']

	path = lines[0]

	data = {}
	poss = []
	zs_elem = []
	for x in lines[2:]:
		node, direc = x.split('=')
		node = node.strip()
		r = []
		d = ''
		for y in direc:
			if y.isalnum():
				d += y
			elif len(d):
				r += [d]
				d = ''
		direc = r

		data[node] = direc

		if node[-1] == 'A':
			poss += [node]
		elif node[-1] == 'Z':
			zs_elem += [node]

	
	# Brute Force
	# while not all([bool(x in zs_elem) for x in poss]):
	# 	n = path[count%len(path)]

	# 	for i in range(len(poss)):
	# 		pos = poss[i]
	# 		if n == 'L':
	# 			poss[i] = data[pos][0]
	# 		else:
	# 			poss[i] = data[pos][1]
	# 	count += 1

	counts = []

	for i in range(len(poss)):
		c = 0
		pos = poss[i]
		# print(pos, end=" => ")
		while pos not in zs_elem:
			n = path[c%len(path)]
			if n == 'L':
				pos = data[pos][0]
			else:
				pos = data[pos][1]
			c += 1
		# print(pos, c)
		counts += [c]

	print(math.lcm(*counts))


if __name__ == '__main__':
	main()


