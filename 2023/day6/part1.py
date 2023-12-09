def main():
	lines = []
	with open("input.txt") as f:
		lines = f.read().split('\n')[:-1]

	# lines = ['Time:      7  15   30', 'Distance:  9  40  200']

	times, dists = lines
	times = *map(int, times.split(':')[1].split()),
	dists = *map(int, dists.split(':')[1].split()),

	res = 1

	for i in range(len(times)):
		t = times[i]
		d = dists[i]

		pos = []
		j = t // 2
		while j * (t - j) > d:
			pos += [j]
			j -= 1

		j = t // 2 + 1
		while j * (t - j) > d:
			pos += [j]
			j += 1
		
		res *= len(pos)

	print(res)

if __name__ == '__main__':
	main()


