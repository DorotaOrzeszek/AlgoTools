def get_integer_matrix(m, n):
	matrix = []
	for i in range(m):
		temp = raw_input()
		row = [int(x) for x in temp.split()]
		if len(row) != n:
			raise Exception("Wrong number of items in row!")
			return None
		else:
			matrix.append(row)
	return matrix

def get_float_matrix(m, n):
	matrix = []
	for i in range(m):
		temp = raw_input()
		row = [float(x) for x in temp.split()]
		if len(row) != n:
			raise Exception("Wrong number of items in row!")
			return None
		else:
			matrix.append(row)
	return matrix

def get_string_matrix(m, n):
  matrix = []
  for i in range(m):
    temp = raw_input()
    row = [x for x in temp.split()]
    if len(row) != n:
      raise Exception("Wrong number of items in row!")
      return None
    else:
      matrix.append(row)
  return matrix
