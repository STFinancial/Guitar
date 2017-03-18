import random as r

from constants import NOTES, NOTES_ONLY_FLATS, NOTES_ONLY_SHARPS

show_number_side = False

def select_set(set_num):
	return [
		NOTES, NOTES_ONLY_FLATS, NOTES_ONLY_SHARPS
	][set_num]

while True:
	n = r.randint(0,11)
	note_set = select_set(r.randint(0,2))
	if show_number_side:
		input(n)
		print(note_set[n])
	else:
		input(note_set[n])
		print(n)
	print()
