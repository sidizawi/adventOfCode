def main():
	"""
	s = source
	se = source + length
	d = destination
	de = destination + length

	x = seed start
	y = seed end

	w = result start
	z = result end


	Cases:
	1) x >= s and y <= se
	s-------x----------y--------se
	d-------w----------z--------de			res = [w, z]

	x---------------------------y
	w---------------------------z

	2) x < s and y > s and y <= se
	x-------s----------y--------se
	--------d----------z--------de			res = [d, z], [x, s[

	x-------s-------------------y
	--------d-------------------z

	3) x >= s and x < se and y > se
	s-------x----------se-------y
	d-------w----------z---------			res = [w, z[, [se, y]

	x------------------se-------y
	d------------------z---------

	4) x < s and y > se
	x-------s----------se-------y
	--------d----------de--------			res = [x, s[, [d, de], ]se, y]

	5) y <= s
	x-------y----------s--------se
	-------------------d--------de			res = [x, y]

	6) x >= se
	s------------se----x---------y
	d------------de---------------			res = [x, y]

	"""
	lines = []
	with open("input.txt") as f:
		lines = f.read().split('\n')[:-1]

	# test
	# lines = ['seeds: 79 14 55 13', '', 'seed-to-soil map:', '50 98 2', '52 50 48', '', 'soil-to-fertilizer map:', '0 15 37', '37 52 2', '39 0 15', '', 'fertilizer-to-water map:', '49 53 8', '0 11 42', '42 0 7', '57 7 4', '', 'water-to-light map:', '88 18 7', '18 25 70', '', 'light-to-temperature map:', '45 77 23', '81 45 19', '68 64 13', '', 'temperature-to-humidity map:', '0 69 1', '1 0 69', '', 'humidity-to-location map:', '60 56 37', '56 93 4']

	_, s = lines[0].split(':')
	s = s.split()
	seeds = [(int(s[i]), int(s[i]) + int(s[i+1])) for i in range(0, len(s), 2)]

	lst = []
	for line in lines:
		if len(line) > 0 and line[0].isdigit():
			d, s, r = map(int, line.split())
			de = d + r
			se = s + r
			state = []
			while len(seeds) > 0:
				x, y = seeds.pop()
				if x >= s and y <= se:
					sx = x - s
					sy = y - s
					lst.append((d + sx, d + sy))
				elif x < s and y > s and y <= se:
					sy = y - s
					lst.append((d, d + sy))
					state.append((x, s))
				elif x >= s and x < se and y > se:
					sx = x - s
					lst.append((d + sx, de))
					state.append((se, y))
				elif x < s and y > se:
					lst.append((d, de))
					state.append((x, s))
					state.append((se, y))
				else:
					state.append((x, y))

			seeds = state
		else:
			seeds.extend(lst)
			lst = []

	seeds.extend(lst)
	res, _ = min(seeds, key=lambda x : x[0])
	print(res)

if __name__ == '__main__':
	main()


