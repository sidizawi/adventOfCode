def main():
	lines = []
	with open("input.txt") as f:
		lines = f.read().split('\n')[:-1]

	#lines = ['seeds: 79 14 55 13', '', 'seed-to-soil map:', '50 98 2', '52 50 48', '', 'soil-to-fertilizer map:', '0 15 37', '37 52 2', '39 0 15', '', 'fertilizer-to-water map:', '49 53 8', '0 11 42', '42 0 7', '57 7 4', '', 'water-to-light map:', '88 18 7', '18 25 70', '', 'light-to-temperature map:', '45 77 23', '81 45 19', '68 64 13', '', 'temperature-to-humidity map:', '0 69 1', '1 0 69', '', 'humidity-to-location map:', '60 56 37', '56 93 4']

	_, s = lines[0].split(':')
	s = s.split()
	seeds = [[int(s[i]), int(s[i]) + int(s[i+1])] for i in range(0, len(s), 2)]

	# name = ""
	state = []
	nseeds = [x for x in seeds]
	for line in lines[2:]:
		if len(line) > 0 and line[0].isdigit():
			d, s, r = list(map(int, line.split()))
			de = d + r
			se = s + r
			#print(name, nseeds, s, se, d, de)
			for x, y in seeds:
				if (x, y) not in state:
					state += [(x, y)]
					if x >= s and y <= se:
						# s-------x-------y-----se
						# d---------------------de
						sx = x - s
						sy = y - s
						idx = nseeds.index([x, y])
						nseeds[idx] = [d + sx, d + sy]
					elif x < s and y>se:
						# x------s--------se-----y
						# -------d--------de-----
						nseeds.remove([x, y])
						nseeds.append([d, de])
						nseeds.append([x, s-1])
						nseeds.append([se+1, y])
					elif x < s and y > s and y<=se:
						# x------s-----y-------se
						# -------d-------------de
						sy = y - s
						nseeds.remove([x, y])
						nseeds.append([x, s-1])
						nseeds.append([d, d+sy])
					elif x >= s and x < se and y > se:
						# s------x-----se-------y
						# d------------de--------
						sx = x - s
						nseeds.remove([x, y])
						nseeds.append([d + sx, de])
						nseeds.append([se+1, y])
					else:
						state.pop()
		else:
			# name = line
			state = []
			seeds = [x for x in nseeds]

	res,_ = min(seeds, key=lambda x: x[0])
	print(res, seeds)

main()


