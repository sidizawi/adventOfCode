def main():
	lines = []
	with open("input.txt") as f:
		lines = f.read().split('\n')[:-1]

	# lines = ['Time:      7  15   30', 'Distance:  9  40  200']

	times, dists = lines
	t = int(''.join(times.split(':')[1].split()))
	d = int(''.join(dists.split(':')[1].split()))

	pos = []
	j = t // 2
	while j * (t - j) > d:
		pos += [j]
		j -= 1

	j = t // 2 + 1
	while j * (t - j) > d:
		pos += [j]
		j += 1

	print(len(pos))

if __name__ == '__main__':
	main()


