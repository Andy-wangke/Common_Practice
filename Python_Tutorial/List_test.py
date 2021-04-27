#test yield expression
def generator():
	for i in range(10):
		x = yield i
		print('current ->',x)

i = generator()
next(i)


