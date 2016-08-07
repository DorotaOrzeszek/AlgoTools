def goto(cycled_list, index):
	l = len(cycled_list)
	if index < l:
		return cycled_list[index]
	else:
		return cycled_list[ index % l ]

def jump(cycled_list, current_index, step):
	l = len(cycled_list)
	if ((current_index + step) < l) and ((current_index + step) >= 0):
		return cycled_list[current_index + step]
	else:
		return cycled_list[ (current_index + step) % l ]
