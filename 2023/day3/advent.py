lines = []
with open("input.txt") as f:
	lines = f.read().split('\n')[:-1]

#lines = ['467..114..', '...*......', '..35..633.', '......#...', '617*......', '.....+.58.', '..592.....', '......755.', '...$.....*', '.664...598']

sm = 0

for j in range(len(lines)):
	d = ""
	f = False
	line = lines[j]
	for i in range(len(line)):
		if line[i].isdigit():
			d += line[i]
			if i > 0:
				if not line[i-1].isdigit() and line[i-1] != '.':
					f = True
				elif j > 0 and not lines[j-1][i-1].isdigit() and lines[j-1][i-1] != '.':
					f = True
				elif j < len(lines) - 1 and not lines[j+1][i-1].isdigit() and lines[j+1][i-1] != '.':
					f = True
			if i < len(line) - 1:
				if not line[i+1].isdigit() and line[i+1] != '.':
					f = True
				elif j > 0 and not lines[j-1][i+1].isdigit() and lines[j-1][i+1] != '.':
					f = True
				elif j < len(lines) - 1 and not lines[j+1][i+1].isdigit() and lines[j+1][i+1] != '.':
					f = True
			if j > 0 and not lines[j-1][i].isdigit() and lines[j-1][i] != '.':
				f = True
			if j < len(lines) - 1 and not lines[j+1][i].isdigit() and lines[j+1][i] != '.':
				f = True
		elif len(d) and f:
			sm += int(d)
			d = ""
			f = False
		else:
			d = ""

	if len(d) and f:
		sm += int(d)

print(sm)

