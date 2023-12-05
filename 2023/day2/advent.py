lines = ""
with open("input.txt", "r") as f:
	lines = f.read()

lines = lines.split('\n')[:-1];

#lines = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', 'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue', 'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red', 'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red', 'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']


sm = 0

for line in lines:
	_, sets = line.split(':')
	b, g, r = 0, 0, 0
	for se in sets.strip().split(";"):
		for x in se.strip().split(","):
			n, c = x.strip().split()
			n = int(n)
			if c == 'blue':
				b = max(n, b)
			elif c == 'red':
				r = max(n, r)
			else:
				g = max(n, g)

	sm += b*g*r

print(sm)

