import random as r

from constants import STRING_NOTES

string_nums = {
	1:7, # E
	2:2, # B
	3:10, # G
	4:5, # D
	5:0, # A
	6:7 # E
}

strings = [6, 5]

while(True):
	string = r.randint(1,6)
	while string not in strings:
		string = r.randint(1,6)
	fret = r.randint(0,16)
	print()
	print(str(string) + " - " + str(fret), end='', flush=True)
	input()
	interval = fret % 12
	print(str(STRING_NOTES[string][interval]) + " OR " + str((string_nums[string] + fret) % 12))
	print(str(STRING_NOTES[string][0]) + " to " + str(STRING_NOTES[string][interval]) + " is " + str(fret) + " steps away.")
