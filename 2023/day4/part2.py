def get_lst(data, x,):

	lst = []
	#print(x, lst)
	for y in data[x]:
		if y == x:
			lst.extend(data[x])
		else:
			for z in data[y][1:]:
				lst.extend(get_lst(data, z))
	#print(x, lst)
	return lst


def main():
	lines = []
	with open("input.txt") as f:
		lines = f.read().split('\n')[:-1]

	#lines = ['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53', 'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19', 'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1', 'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83', 'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36', 'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']

	data = {}

	for line in lines:
		card, d = line.split(':')
		_, c = card.strip().split()
		c = int(c)
		win, have = d.strip().split('|')
		win = win.strip().split()
		have = have.strip().split()
		count = 0
		for w in win:
			if w in have:
				count += 1
		
		data[c] = [c + i for i in range(count + 1)]

	res = []

	for x in data:
		res += get_lst(data, x)

	print(len(res))

main()


