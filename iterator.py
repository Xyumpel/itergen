class FlatIterator:

    def __init__(self, nested_list):
        self.nested_list = nested_list
    
    def __iter__(self):
        self.i = -1
        return self

    def __next__(self):
        self.i += 1
        if self.i == len(self.nested_list,):
            raise StopIteration
        letter = self.nested_list[self.i]
        return letter

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	['g', 'h', 'i'],
]

def one_list(nested_list):
    while isinstance(nested_list[0], str) == False:
        nested_list = sum(nested_list,[])
    return nested_list

for item in FlatIterator(one_list(nested_list)):
	print(item)