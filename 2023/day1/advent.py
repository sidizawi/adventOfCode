lines = ""
with open('input.txt', 'r') as f:
	lines = f.read()

lines = lines.lower().split('\n')[:-1]

#lines = ['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen']

l = {
	'zero': '0',
	'one': '1',
	'two': '2',
	'three': '3',
	'four': '4',
	'five': '5',
	'six': '6',
	'seven': '7',
	'eight': '8',
	'nine': '9',
}
s = 0

for line in lines:
	d = []
	for i in range(len(line)):
		x = line[i]
		if x.isdigit():
			d += [x]
		for y in l:
			if x == y[0] and i + len(y) <= len(line) and line[i:i+len(y)] == y:
				d += [l[y]]

	if len(d):
		f = int(d[0] + d[-1])
		print(line, f)
		s += f

print(s)

