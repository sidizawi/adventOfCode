import math

TILES = {
	'|': ['N', 'S'],
	'-': ['E', 'W'],
	'L': ['N', 'W'],
	'J': ['N', 'E'],
	'7': ['S', 'E'],
	'F': ['S', 'W'],
}

def next_pos(lines, pos, n):
	y, x = pos
	symb = lines[y][x]
	if symb == 'S':
		direc = []
		if x > 0 and lines[y][x-1] in '-LF':
			direc += ['E']
		if y > 0 and lines[y-1][x] in '|F7':
			direc += ['N']
		if x < len(lines[y]) - 1 and lines[y][x+1] in '-7J':
			direc += ['W']
		if y < len(lines) - 1 and lines[y+1][x] in '|JL':
			direc += ['S']

		symbs = [a for a in TILES if all([b in TILES[a] for b in direc])]
		if len(symbs) != 1:
			return (n, pos)
		
		symb = symbs[0]

	direc = TILES[symb]
	if y > 0 and ((n == 'N' and symb == '|') or ('N' in direc and n != 'S')):
		y -= 1
		n = 'N'
	elif x < len(lines[y]) - 1 and ((n == 'W' and symb == '-') or ('W' in direc and n != 'E')):
		x += 1
		n = 'W'
	elif y < len(lines) - 1 and ((n == 'S' and symb == '|') or ('S' in direc and n != 'N')):
		y += 1
		n = 'S'
	elif x > 0 and ((n == 'E' and symb == '-') or ('E' in direc and n != 'W')):
		x -= 1
		n = 'E'

	# print('fin de next pos', y, x, n, lines[y][x])
	return (n, [y, x])
		

def main():
	lines = []
	with open("input.txt") as f:
		lines = [list(x) for x in f.read().split('\n')[:-1]]

	# lines = [
	# 	['.', '.', '.', '.', '.'], 
	# 	['.', 'F', '-', '7', '.'], 
	# 	['.', 'S', '.', '|', '.'], 
	# 	['.', 'L', '-', 'J', '.'], 
	# 	['.', '.', '.', '.', '.']
	# ]

	# lines = [
	# 	['.', '.', 'F', '7', '.'], 
	# 	['.', 'F', 'J', '|', '.'], 
	# 	['S', 'J', '.', 'L', '7'], 
	# 	['|', 'F', '-', '-', 'J'], 
	# 	['L', 'J', '.', '.', '.']
	# ]


	i = 0
	pos = None
	while not pos:
		if 'S' in lines[i]:
			pos = [i, lines[i].index('S')]
		i += 1
	
	finished = False
	count = 0
	n = 'N'
	while not finished:
		n, pos = next_pos(lines, pos, n)

		if lines[pos[0]][pos[1]] == 'S':
			finished = True
		
		count += 1

	print(math.ceil(count / 2))

if __name__ == '__main__':
	main()


