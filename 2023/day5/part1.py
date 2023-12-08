def main():
	lines = []
	with open("input.txt") as f:
		lines = f.read().split('\n')[:-1]

	#lines = ['seeds: 79 14 55 13', '', 'seed-to-soil map:', '50 98 2', '52 50 48', '', 'soil-to-fertilizer map:', '0 15 37', '37 52 2', '39 0 15', '', 'fertilizer-to-water map:', '49 53 8', '0 11 42', '42 0 7', '57 7 4', '', 'water-to-light map:', '88 18 7', '18 25 70', '', 'light-to-temperature map:', '45 77 23', '81 45 19', '68 64 13', '', 'temperature-to-humidity map:', '0 69 1', '1 0 69', '', 'humidity-to-location map:', '60 56 37', '56 93 4']

	_, s = lines[0].split(':')
	seeds = list(map(int, s.split()))

	#print(seeds)
	name = ""
	state = []
	for line in lines[2:]:
		if len(line) > 0 and line[0].isdigit():
			d, s, r = list(map(int, line.split()))
			for i in range(len(seeds)):
				x = seeds[i]
				if x >= s and x < s+r and i not in state:
					seeds[i] = d + (x - s)
					state += [i]
					#print(x, d, s, r)
			#print(name, seeds, line)
		else:
			name = line
			state = []

	print(min(seeds))

main()


