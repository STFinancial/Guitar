import random as r

from constants import NOTES

note_nums = {
	'A':0,
	'A#/Bb':1,
	'B':2,
	'C':3,
	'C#/Db':4,
	'D':5,
	'D#/Eb':6,
	'E':7,
	'F':8,
	'F#/Gb':9,
	'G':10,
	'G#/Ab':11,
}

num_notes = {
	0:'A',
	1:'A#/Bb',
	2:'B',
	3:'C',
	4:'C#/Db',
	5:'D',
	6:'D#/Eb',
	7:'E',
	8:'F',
	9:'F#/Gb',
	10:'G',
	11:'G#/Ab',
}

show_number_side = True

while True:
	n = r.randint(0,11)
	if show_number_side:
		input(n)
		print(NOTES[n])
	else:
		input(note_nums[n])
		print(n)
	print()

