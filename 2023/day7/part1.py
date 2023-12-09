from functools import cmp_to_key

CARDS = 'AKQJT98765432'

def hand_value(hand):
	if len(set(hand)) == 1:
		# Five of a kind
		return 7
	elif sorted([hand.count(x) for x in set(hand)]) == [1, 4]:
		# Four of a kind
		return 6
	elif sorted([hand.count(x) for x in set(hand)]) == [2, 3]:
		# Full house
		return 5
	elif sorted([hand.count(x) for x in set(hand)]) == [1, 1, 3]:
		# Three of a kind
		return 4
	elif sorted([hand.count(x) for x in set(hand)]) == [1, 2, 2]:
		# Two pair
		return 3
	elif len(set(hand)) == 4:
		# One pair
		return 2
	# High card
	return 1

def compare_hands(h1, h2):
	h1_value = hand_value(h1[0])
	h2_value = hand_value(h2[0])

	if h1_value == h2_value:
		i = 0
		while i < len(h1[0]) and h1[0][i] == h2[0][i]:
			i += 1
		if i == len(h1[0]):
			return 0
		elif CARDS.index(h1[0][i]) < CARDS.index(h2[0][i]):
			return 1
		return -1
	elif h1_value > h2_value:
		return 1
	return -1

def main():
	lines = []
	with open("input.txt") as f:
		lines = f.read().split('\n')[:-1]

	# lines = ['32T3K 765', 'T55J5 684', 'KK677 28', 'KTJJT 220', 'QQQJA 483']

	lines = [(x.split()[0], int(x.split()[1])) for x in lines]

	rankings = sorted(lines, key=cmp_to_key(compare_hands))

	res = 0
	for i in range(len(rankings)):
		# print(rankings[i])
		res += rankings[i][1] * (i + 1)
	print(res)

if __name__ == '__main__':
	main()


