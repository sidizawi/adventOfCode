def get_nbr(lines, i, j):
	n = ''
	while j > 0 and lines[i][j].isdigit():
		j-=1
	if not lines[i][j].isdigit():
		j+=1
	start = j
	while j < len(lines[i]) and lines[i][j].isdigit():
		n += lines[i][j]
		j+=1
	end = j - 1
	#print(n, start, end)
	return (int(n), start, end)

def main():
	lines = []
	with open("input.txt") as f:
		lines = f.read().split('\n')[:-1]

	#lines = ['467..114..', '...*......', '..35..633.', '......#...', '617*......', '.....+.58.', '..592.....', '......755.', '...$.....*', '.664...598']


	sm = 0

	for i in range(len(lines)):
		line = lines[i]
		for j in range(len(line)):
			if line[j] == '*':
				lst = []
				if (i > 0 and lines[i-1][j].isdigit()):
					lst.append(get_nbr(lines, i-1, j))
				if (i > 0 and j > 0 and lines[i-1][j-1].isdigit()):
					lst.append(get_nbr(lines, i-1, j-1))
				if (i > 0 and j < len(line) - 1 and lines[i-1][j+1].isdigit()):
					lst.append(get_nbr(lines, i-1, j+1))
				if (j > 0 and lines[i][j-1].isdigit()):
					lst.append(get_nbr(lines, i, j-1))
				if (j < len(line) - 1 and lines[i][j+1].isdigit()):
					lst.append(get_nbr(lines, i, j+1))
				if (i < len(lines) - 1 and lines[i+1][j].isdigit()):
					lst.append(get_nbr(lines, i+1, j))
				if (i < len(lines) - 1 and j > 0 and lines[i+1][j-1].isdigit()):
					lst.append(get_nbr(lines, i+1, j-1))
				if (i < len(lines) - 1 and j < len(line) - 1 and lines[i+1][j+1].isdigit()):
					lst.append(get_nbr(lines, i+1, j+1))
				lst = list(set(lst))
				if len(lst) == 2:
					#print(lst)
					sm += lst[0][0] * lst[1][0]

	print(sm)

main()

