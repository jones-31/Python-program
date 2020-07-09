def filter_list(input_value):

	for i in rejected_items:
		if i in input_value:
			input_value.remove(i)

	print(input_value)

input_value = ["impolite", "cows", "undress", "rule", "illustrious", "beam", "helpless", "gold", "hair",
"vacuous", "help", "guess", "squalid", "wonderful", "memorise", "present", "painful", "brake", "sand",
"lip", "rainstorm", "talk", "abashed", "box", "partner", "chop", "tenuous", "robin", "trees", "moor",
"hunt", "pack", "old-fashioned"]

rejected_items = ["cows", "partner", "wonderful", "rainstorm", "pack", "painful"]

filter_list(input_value)
