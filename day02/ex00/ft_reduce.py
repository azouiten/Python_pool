


def ft_reduce(fun, iter):
	if len(iter) == 0:
		return
	result = iter[0]
	for elem in iter[1:]:
		result = fun(result, elem)
	return result