import random as r

string_notes = {
	1:['E','F','F# / Gb','G','G# / Ab','A','A# / Bb','B','C','C# / Db','D','D# / Eb','E',],
	2:['B','C','C# / Db','D','D# / Eb','E','F','F# / Gb','G','G# / Ab','A','A# / Bb','B',],
	3:['G','G# / Ab','A','A# / Bb','B','C','C# / Db','D','D# / Eb','E','F','F# / Gb','G',],
	4:['D','D# / Eb','E','F','F# / Gb','G','G# / Ab','A','A# / Bb','B','C','C# / Db','D',],
	5:['A','A# / Bb','B','C','C# / Db','D','D# / Eb','E','F','F# / Gb','G','G# / Ab','A',],
	6:['E','F','F# / Gb','G','G# / Ab','A','A# / Bb','B','C','C# / Db','D','D# / Eb','E',],
}

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
	print(str(string_notes[string][interval]) + " OR " + str((string_nums[string] + fret) % 12))
	print(str(string_notes[string][0]) + " to " + str(string_notes[string][interval]) + " is " + str(fret) + " steps away.")
