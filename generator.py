def flat_generator(nested_list): 
    for a in nested_list:
        yield a

def one_list(nested_list):
    while isinstance(nested_list[0], str) == False:
        nested_list = sum(nested_list,[])
    return nested_list


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	['g', 'h', 'i'],
]
for item in  flat_generator(one_list(nested_list)):
	print(item)