def get_integer_list(m = ""):
	temp = raw_input(m)
	integer_list = [int(x) for x in temp.split()]
	return integer_list

def get_float_list(m = ""):
	temp = raw_input(m)
	float_list = [float(x) for x in temp.split()]
	return float_list

def get_string_list(m = ""):
	temp = raw_input()
	string_list = [x for x in temp.split()]
	return string_list

