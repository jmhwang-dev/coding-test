# not solved
def camping(L=5, P=8, V=20):
	count = V // P * L
	count += V % P
	return count

input_list = []
while True:
	int_input = list(map(int, input().split()))
	filter_output = list(filter(lambda x: False if x == 0 else True, int_input))
	if len(filter_output) == 0:
		break
	input_list.append(int_input)

for i, _list in enumerate(input_list, 1):
	L, P, V = _list
	print("Case {}: {}".format(i, camping(L, P, V)))