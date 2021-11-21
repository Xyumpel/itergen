class FlatIterator:

    def __init__(self, nested_list):
        self.nested_list = sum(nested_list,[])
    
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

for item in FlatIterator(nested_list):
	print(item)